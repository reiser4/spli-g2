import utils
import pyprimes
import fractions
import sys
import time

if __name__ == "__main__":

    if len(sys.argv) != 5:
        sys.exit("Per eseguire correttamente: 'python main.py filename big_number nth_prime_for_A nth_prime_for_B'")
    else:
        filename = sys.argv[1]
        big_number1 = int(sys.argv[2])
        big_number2 = int(sys.argv[3])
        nthprime = int(sys.argv[4])
    
    tstart = time.time()
    
    p = utils.calculateP(big_number1)
    q = utils.calculateP(big_number2)
    n = p * q
    fn = (p-1) * (q-1)

    filename_ori = filename
    filename, fileext = filename.rsplit('.', 1)
    filename_dec = filename + "_dec." + fileext

    e = utils.calculateEncryptionKey(nthprime, fn)
    #eB = utils.calculateEncryptionKey(nthprimeB, p)
    d = utils.modinv(e, fn)
    #dB = utils.modinv(eB, fp)
    print "Prime number:", '{0:,}'.format(p)
    print "Encryption key A:", '{0:,}'.format(e)
    #print "Encryption key B:", '{0:,}'.format(eB)
    print "Decryption key A:", '{0:,}'.format(d)
    #print "Decryption key B:", '{0:,}'.format(dB)

    (header, body) = utils.splitToHeaderBody(filename_ori)
    
    body = utils.char2int(body, n)

    print "A -encrypt-> B"
    body1AtoB = utils.algorithm(body, e, n)
    utils.writeFileTmp(filename + "_eA." + fileext, header, body1AtoB)
    
    #print "B -encrypt-> A"
    #body1BtoA = utils.algorithm(body1AtoB, eB, p)
    #utils.writeFileTmp(filename + "_eB." + fileext, header, body1BtoA)
    
    print "A -decrypt-> B"
    body2AtoB = utils.algorithm(body1AtoB, d, n)
    utils.writeFileTmp(filename + "_dA." + fileext, header, body2AtoB)
    
    #print "B -decrypt-> A"
    #body2BtoA = utils.algorithm(body2AtoB, dB, p)
    #utils.writeFile(filename_dec, header, body2BtoA)
    
    if utils.md5same(utils.md5(filename_ori), utils.md5(filename_dec)):
        print "File decodificato correttamente"
    else:
        print "Il file decodificato e' diverso dall'originale'"

    print "Tempo impiegato:", round(time.time() - tstart, 2), "secondi"
