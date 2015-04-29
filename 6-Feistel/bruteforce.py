import itertools
import utils
import time
import sys
import marco

if __name__ == "__main__":
    if len(sys.argv) == 4:
        len_key = int(sys.argv[1])
        filename_padded = sys.argv[2]
        filename_encrypt = sys.argv[3]
    elif not len(sys.argv) == 1:
        sys.exit("Per eseguire correttamente: 'python bruteforce.py len_key filename_padded filename_encrypt'")
    print "Welcome to the party\n" 
    print "Inizio l'attacco"
    print "Attendi..."
    filename_encrypt = "file-crypted.tga"
    filename_padded = "file-padded.tga"
    start = time.time()
    for key in map(''.join, itertools.product('01', repeat=len_key)):
        filename_decrypt = marco.create_decrypted_file(key, filename_encrypt)
        md5_padded = utils.md5(filename_padded)
        md5_decrypt = utils.md5(filename_decrypt)    
        if utils.md5same(md5_padded, md5_decrypt):
            print
            print "md5 del file '" + filename_padded + "':\t" + md5_padded
            print "md5 del file '" + filename_decrypt + "':\t" + md5_decrypt
            time = round(time.time() - start, 2)
            print "La chiave del tesoro e': '" + str(key) + "', lunghezza " + str(len(key)) + " bit"
            print "E' stata trovata in: " + str(time) + " secondi"
            break
        else:
            print "Ho provato con chiave: '" + str(key) + "'"
    print "\nJob done, goodbye"
