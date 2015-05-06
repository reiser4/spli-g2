import itertools
import utils
import time
import sys
import pyprimes

if __name__ == "__main__":
    filename_ori = "lena.tga"
    filename_encrypt = "lena_eA.tga"
    filename_bruteforce = "lena_bruteforce.tga"
    n = int(sys.argv[1])
    print "Welcome to the party\n" 
    print "Inizio l'attacco"
    print "Attendi..."
    
    (header, body) = utils.splitToHeaderBody(filename_encrypt)
    #body = utils.char2int(body, n)
    
    
    intfile = open(filename_encrypt + "-int",'rb')
    cbody = intfile.read()
    ibody = cbody.split(" ")
    body = list()
    for integer in ibody:
        if integer != "":
            body.append(int(integer))
    intfile.close()
    
    
    md5_ori = utils.md5(filename_ori)
    start = time.time()
    
    for key in range(970, 1024):
        print "Provo con la chiave: '" + str(key) + "'"
        body1 = utils.algorithm(body, key, n)
        utils.writeFileTmp(filename_bruteforce, header, body1)
        md5_bruteforce = utils.md5(filename_bruteforce)
        if utils.md5same(md5_ori, md5_bruteforce):
            print
            print "md5 del file '" + filename_ori + "':\t\t" + md5_ori
            print "md5 del file '" + filename_bruteforce + "':\t" + md5_bruteforce
            print "La chiave del tesoro e': '" + str(key) + "'"
            print "E' stata trovata in: " + str(round(time.time() - start, 2)) + " secondi"
            break
        else:
            print "L'attacco non e' andato a buon fine"
            print
    print "\nJob done, goodbye"
