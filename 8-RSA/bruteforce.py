import itertools
import utils
import time
import sys
import pyprimes

def attack(filename_pad, filename_enc, filename_bru, n, start_dec, dim_blocco, header, body_enc):
    #print "Welcome to the party"
    print "Start attack"
    print "Attendi..."

    md5_pad = utils.md5(filename_pad)
    start = time.time()

    for key in range(start_dec, start_dec + 10):
        print "Provo con la chiave: '" +  '{0:,}'.format(key) + "'"
        body_bru = utils.algorithm(body_enc, key, n)
        utils.writeFile(filename_bru, header, body_bru)
        md5_bru = utils.md5(filename_bru)
        if utils.md5same(md5_pad, md5_bru):
            print
            print "md5 del file '" + filename_pad + "':\t" + md5_pad
            print "md5 del file '" + filename_bru + "':\t" + md5_bru
            print "La chiave del tesoro e': '" + '{0:,}'.format(key) + "'"
            print "E' stata trovata in: " + str(round(time.time() - start, 2)) + " secondi"
            break
        else:
            print "L'attacco non e' andato a buon fine"
            print
    print "\nJob done, goodbye"
