import socket
import sys
import hashlib

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
    
    while True:
        input = raw_input ("Inserire la chiava per la decodifica: ")
        if input.isdigit():
            key = int(input)
            if key > 0 and key <= 26:
                break
    
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
        #print "Connected with " + clientaddress[0] + ":" + clientaddress[1]
        
        message_encrypt = ''
        while True:
            message = clientsocket.recv(buff)
            if not message:
                break
            else:
                message_encrypt += message
        
        foutput = open(file_encrypt, 'wb')
        foutput.write(message_encrypt)
        foutput.flush()
        foutput.close()
        
    except:
        raise
        sys.exit()
        
    finally:
        serversocket.close()
    
    print 'Ho ricevuto un file, chiudo client e server socket'
    
    print "Calcolo md5 del file appena ricevuto:\t",
    md5_file_receive = hashlib.md5(open(file_encrypt, 'rb').read()).hexdigest()
    print md5_file_receive
    
    print "Calcolo md5 del file originale:\t\t",
    md5_file_original = hashlib.md5(open(file_original_encrypt, 'rb').read()).hexdigest()
    print md5_file_original
    
    if md5_file_receive == md5_file_original:
        print "Yeah, i due file sono uguali"
    else:
        print "Ops, i due file non sono uguali"
        sys.exit()
    
    print
    
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
    
    foutput = open(file_decrypt, 'w')
    foutput.write(message_decrypt)
    foutput.flush()
    foutput.close()
    
    print "Calcolo md5 del file decodificato:\t",
    md5_file_decrypt = hashlib.md5(open(file_decrypt, 'rb').read()).hexdigest()
    print md5_file_decrypt
    
    print "Calcolo md5 del file originale pulito:\t",
    md5_file_original_clean = hashlib.md5(open(file_original_clean, 'rb').read()).hexdigest()
    print md5_file_original_clean
    
    if md5_file_decrypt == md5_file_original_clean:
        print "Yeah, i due file sono uguali"
    else:
        print "Ops, i due file non sono uguali"
        sys.exit()
    
    print "Well done, goodbye"