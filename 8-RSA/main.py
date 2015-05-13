import utils
import pyprimes
import fractions
import sys
import time
import bruteforce

if __name__ == "__main__":

    if len(sys.argv) != 5:
        sys.exit("Per eseguire correttamente: 'python main.py filename big_number1 big_number2 nth_prime'")
    else:
        filename = sys.argv[1]
        big_number1 = int(sys.argv[2])
        big_number2 = int(sys.argv[3])
        nthprime = int(sys.argv[4])

    # per eseguire con dim_blocco = 8 chiudere chrome ed eseguire il seguente comando
    # python main.py lena.tga 9989999995 99999999995 10000000
    dim_blocco = 4

    tstart = time.time()

    p = utils.calculateP(big_number1)
    q = utils.calculateP(big_number2)
    n = p * q
    fn = (p-1) * (q-1)

    filename_ori = filename
    filename, fileext = filename.rsplit('.', 1)
    filename_enc = filename + "_encrypted." + fileext
    filename_dec = filename + "_decrypted." + fileext
    filename_pad = filename + "_paddata." + fileext

    e = utils.calculateEncryptionKey(nthprime, fn)
    d = utils.modinv(e, fn)
    print "Prime number p:", '{0:,}'.format(p)
    print "Prime number q:", '{0:,}'.format(q)
    print "N:", '{0:,}'.format(n)
    print "Encryption key:", '{0:,}'.format(e)
    print "Decryption key:", '{0:,}'.format(d)

    (header, body) = utils.splitToHeaderBody(filename_ori)
    body = utils.padding(body, dim_blocco)
    utils.writePadding(filename_pad, header, body)
    body_list = utils.chunkBody(body, dim_blocco)
    body_num = utils.char2int(body_list, n) #TODO: Questo verra' cancellato
    #print "Len file paddato: ", len(body_num)
    print "Encryption: start",
    body_enc = utils.algorithm(body_num, e, n) # Qui passiamo la lista di blocchi
    utils.writeFileDec(filename_enc, header, body_enc, dim_blocco)
    #print max(body1AtoB)
    print " -> done"
    #print "Len encrypted file: ", len(body_enc) # gia'' trasformata in interi

    print "Decryption: start",
    body_dec = utils.algorithm(body_enc, d, n)
    #print len(body2AtoB)
    utils.writeFile(filename_dec, header, body_dec)
    print " -> done"
    #print "Len decrypted file: ", len(body_dec)

    if utils.md5same(utils.md5(filename_pad), utils.md5(filename_dec)):
        print "File decodificato correttamente"
    else:
        print "ERRORE: Il file decodificato e' diverso dall'originale'"

    print "Tempo impiegato:", round(time.time() - tstart, 2), "secondi"

    print "\n-----------------------------------------------------------------\n"
    bruteforce.attack(filename_pad, filename_enc, filename + "_bruteforce." + fileext, n, d-3, dim_blocco, header, body_enc)
