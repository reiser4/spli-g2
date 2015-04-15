import sys 
import os

def encrypt(key, file_input, file_output):
    finput = open(file_input, 'r')
    foutput = open(file_output, 'w')
    message = finput.read()
    finput.close()
    
    translated = ''
    
    for symbol in message:
        c = (ord(symbol)+key) % 126
        if c < 32: 
            c += 31
        translated += chr(c)
    
    foutput.write(translated)
    foutput.flush()
    foutput.close()
    
def decrypt(key, file_input, file_output):
    finput = open(file_input, 'r')
    foutput = open(file_output, 'w')
    message = finput.read()
    finput.close()
    
    translated = ''
    
    for symbol in message:
        c = (ord(symbol)-key) % 126
        if c < 32:
            c += 95
        translated += chr(c)
        
    foutput.write(translated)
    foutput.flush()
    foutput.close()


if __name__ == "__main__":
    
    if len(sys.argv) != 3:
        print "ERROR: 'python caesar.ciphers.ascii.printable.character.py file_name.txt chiave'"
        sys.exit(0)
    
    file = sys.argv[1]
    key = int(sys.argv[2])
    
    print "Nome file: " + file
    print "Chiave: " + str(key)
    print ""
    
    if not os.path.isfile(file):
        print "\nERROR: il file non esiste"
        sys.exit(0)
        
    file_split = file.split(".")
        
    file_name = file_split[0]
    file_ext = file_split[1]
    if file_ext != "txt":
        print "Error: the name of file is wrong"
        sys.exit(0)

    file_encrypt = file_name + "_encrypt.txt" 
    file_decrypt = file_name + "_decrypt.txt"
    file_bruteforce = file_name + "_bruteforce.txt"
    
    if os.path.isfile(file_bruteforce):
        os.remove(file_bruteforce)
    
    encrypt(key, file, file_encrypt)
    decrypt(key, file_encrypt, file_decrypt)
