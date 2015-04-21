import hashlib


def md5same(md5_1, md5_2):
    if md5_1 == md5_2:
        print "Yeah, i due file sono uguali"
    else:
        print "Ops, i due file non sono uguali -> EXIT"
        sys.exit()
    
def md5(filename):
    return hashlib.md5(open(filename, 'rb').read()).hexdigest()

def algorithm(filename_encrypt, key):
    finput = open(filename_encrypt, 'r')
    message_encrypt = finput.read()
    finput.close()
    message_decrypt = ''
    for char in message_encrypt:
        if char.isalpha(): 
            num = ord(char) - key                
            if num > ord('z'):
                num -= ord('z') - ord('a') + 1
            elif num < ord('a'):
                num += ord('z') - ord('a') + 1
            message_decrypt += chr(num)
        else:
            message_decrypt += char
    return message_decrypt
