import socket
import sys
from string import ascii_lowercase
import brute_force
import utils


if __name__ == '__main__':

    if len(sys.argv) != 3:
        sys.exit('ERROR, usage: python attack.py PORT IP_GIULIO')

    if not sys.argv[1].isdigit():
        sys.exit('ERROR, usage: python attack.py PORT IP_GIULIO')
    
    HOST = ''
    PORT = int(sys.argv[1])
    BUFF = 512
    IP_GIULIO = sys.argv[2]
    PORT_GIULIO = 9998

    filename_bruteforce = "message_bruteforce.txt"
    filename_decrypt = "message_decrypt_bruteforce.txt"
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (HOST, PORT)
    sock.bind(server_address)
    
    sock.listen(3)

    print 'Waiting incoming connections...'
    connection, addr = sock.accept()        
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
    file = open(filename_bruteforce, 'wb');
    l = connection.recv(BUFF)
    while (l):
        file.write(l)
        l = connection.recv(BUFF)
                  
    file.close();
    print("File saved in folder. \n Stopping connection..")
    connection.close()
    sock.close()

    print "Calcolo md5 del file codificato appena ricevuto: ", utils.md5(filename_bruteforce)

    print("Sending file to Giulio..")
    file_bruteforce = open(filename_bruteforce, 'rb'); 
    message = file_bruteforce.read()
    file_bruteforce.close()
    print ("Connecting to Giulio..")
    sock_send = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = (IP_GIULIO, PORT_GIULIO)
    sock_send.connect(address);
    print ("Connected to Giulio , sending file..")

    try:
        sock_send.send(message);
        print ("File spedito correttamente")
    finally:
        sock_send.close()

    key = brute_force.find_key(filename_bruteforce)
    print "\nThe key is : ", key

    foutput = open(filename_decrypt, 'w')
    foutput.write(utils.algorithm(filename_bruteforce, key))
    foutput.flush()
    foutput.close()

    print "Calcolo md5 del file decodificato con bruteforce: ", utils.md5(filename_decrypt)
    
    print("\n END");
    
