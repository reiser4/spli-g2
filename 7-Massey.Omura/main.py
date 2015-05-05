import utils
import pyprimes
import fractions
import sys

if __name__ == "__main__":

    if len(sys.argv) != 5:
        sys.exit("Per eseguire correttamente: 'python main.py filename big_number nth_prime_for_A nth_prime_for_B'")
    else:
        filename = sys.argv[1]
        big_number = int(sys.argv[2])
        nthprimeA = int(sys.argv[3])
        nthprimeB = int(sys.argv[4])

    p = utils.calculateP(big_number)
    fp = p-1

    filename_ori = filename
    filename, fileext = filename.rsplit('.', 1)
    print filename,fileext
    eA = utils.calculateEncryptionKey(nthprimeA, p)
    eB = utils.calculateEncryptionKey(nthprimeB, p)
    dA = utils.modinv(eA, fp)
    dB = utils.modinv(eB, fp)
    print "Encryption key A:", '{0:,}'.format(eA)
    print "Encryption key B:", '{0:,}'.format(eB)
    print "Decryption key A:", '{0:,}'.format(dA)
    print "Decryption key B:", '{0:,}'.format(dB)
    print "Prime number:", '{0:,}'.format(p)

    (header, body) = utils.splitToHeaderBody(filename_ori)
    
    body = utils.char2int(body, p)

    print "A -encrypt-> B"
    body1AtoB = utils.algorithm(body, eA, p)
    print "B -encrypt-> A"
    body1BtoA = utils.algorithm(body1AtoB, eB, p)
    print "A -decrypt-> B"
    body2AtoB = utils.algorithm(body1BtoA, dA, p)
    print "B -decrypt-> A"
    body2BtoA = utils.algorithm(body2AtoB, dB, p)
    
    filename_dec = filename + "_dec." + fileext
    utils.writeFile(filename_dec, header, body2BtoA)
    
    if utils.md5same(utils.md5(filename_ori), utils.md5(filename_dec)):
        print "File decodificato correttamente"
    else:
        print "Il file decodificato e' diverso dall'originale'"

