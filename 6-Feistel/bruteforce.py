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
    md5_padded = utils.md5(filename_padded)
    start = time.time()
    for key in map(''.join, itertools.product('01', repeat=len_key)):
        print "Provo con la chiave: '" + str(key) + "'"
        filename_decrypt = marco.create_decrypted_file(key, filename_encrypt)
        md5_decrypt = utils.md5(filename_decrypt)
        if utils.md5same(md5_padded, md5_decrypt):
            print
            print "md5 del file '" + filename_padded + "':\t\t" + md5_padded
            print "md5 del file '" + filename_decrypt + "':\t" + md5_decrypt
            timeexe = round(time.time() - start, 2)
            print "La chiave del tesoro e': '" + str(key) + "', lunghezza " + str(len(key)) + " bit"
            print "E' stata trovata in: " + str(timeexe) + " secondi"
            break
        else:
            print "L'attacco non e' andato a buon fine"
            print
    print "\nJob done, goodbye"
