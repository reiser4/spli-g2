
import socket
import sys

# USE   marco@marco-Aspire-V5-571G:~ attack.py PORT IP_GIULIO

if __name__ == '__main__':

    HOST = ''
    PORT = sys.argv[1]
    IP_GIULIO = sys.argv[2]

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('', PORT)
    sock.bind(server_address)
    
    sock.listen(3)

    while True:

        print 'Waiting incoming connections...'
        connection, addr = sock.accept()        
        print 'Connected with ' + addr[0] + ':' + str(addr[1])
        file = open("/home/marco/Python/message_crypted.txt", 'w+');
        l = connection.recv(128)

        while (l):
            file.write(l)
            l = connection.recv(128)
          
            
        file.close();
        print("File saved in folder. \n Stopping connection..")
        connection.close()
        sock.close()


        print("Sending file to Giulio..")
        file = open("/home/marco/Python/message_crypted.txt", 'r+'); 
        str = file.read(512)
        print ("Connecting to Giulio..")
        sock_send = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        address = (IP_GIULIO,PORT)
        sock_send.connect(address);
        print ("Connected to Giulio , sending file..")

        try:
            sock_send.write(str);
            print ("ok")
        finally:
            sock_send.close()
    
    print("END");
