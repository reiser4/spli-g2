import socket
import sys
import hashlib

def md5same(md5_1, md5_2):
    if md5_1 == md5_2:
        print "Yeah, i due file sono uguali"
    else:
        print "Ops, i due file non sono uguali -> EXIT"
        sys.exit()
    
def md5(filename):
    return hashlib.md5(open(filename, 'rb').read()).hexdigest()

def writefile(filename, message, mod=None):
    if mod == 'b':
        foutput = open(filename, 'wb')
    elif not mod:
        foutput = open(filename, 'w')
    else:
        print "ERRORE nella chiamata della funzione 'writefile'"
        sys.exit()
    foutput.write(message)
    foutput.flush()
    foutput.close()
    
if __name__ == "__main__":
    
    print "Welcome to the party" 
    print
    
    file_name = "message"
    file_ext = "txt"
    file_encrypt = file_name + '_encrypt.' + file_ext
    file_decrypt = file_name + '_decrypt.' + file_ext
    file_original = "pg100.txt"
    file_original_encrypt = "pg100.txt-cifrato"
    file_original_clean = "pg100.txt-pulito"

    try:
        #host = '::'
        host = ''
        port = 9999
        buff = 512
     
        address = (host, port)
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print 'Socket created'
        serversocket.bind(address)
        print 'Socket bind complete'
        serversocket.listen(1)
        print 'Server in ascolto %s porta %s' % address
        
        print "In attesa di connessione..."
        (clientsocket, clientaddress) = serversocket.accept()
        print "Connected with " + clientaddress[0] + ":" + str(clientaddress[1])
        
        message_encrypt = ''
        while True:
            message = clientsocket.recv(buff)
            if not message:
                break
            else:
                message_encrypt += message
        
        writefile(file_encrypt, message_encrypt, 'b')
        
    except:
        raise
        sys.exit()
        
    finally:
        serversocket.close()
    print 'Ho ricevuto un file, chiudo client e server socket'

    print "Calcolo md5 del file appena ricevuto:\t",
    md5_file_receive = md5(file_encrypt)
    print md5_file_receive
    
    print
    
    while True:
        input = raw_input ("Inserire la chiava per la decodifica: ")
        if input.isdigit():
            key = int(input)
            if key > 0 and key <= 26:
                break
    
    finput = open(file_encrypt, 'r')
    message_encrypt = finput.read()
    finput.close()
    
    message_decrypt = ''
    prova = True
    
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
    
    writefile(file_decrypt, message_decrypt)

    print "Calcolo md5 del file decodificato:\t",
    md5_file_decrypt = md5(file_decrypt)
    print md5_file_decrypt
    
    print "Well done, goodbye"
