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
        big_number = int(sys.argv[2])
        nthprimeA = int(sys.argv[3])
        nthprimeB = int(sys.argv[4])

    dim_blocco = 4

    tstart = time.time()

    p = utils.calculateP(big_number)
    fp = p-1

    filename_ori = filename
    filename, fileext = filename.rsplit('.', 1)
    filename_dec = filename + "_dec." + fileext
    filename_pad = filename + "_paddata." + fileext

    eA = utils.calculateEncryptionKey(nthprimeA, p)
    eB = utils.calculateEncryptionKey(nthprimeB, p)
    dA = utils.modinv(eA, fp)
    dB = utils.modinv(eB, fp)
    print "Prime number:", '{0:,}'.format(p)
    print "Encryption key A:", '{0:,}'.format(eA)
    print "Encryption key B:", '{0:,}'.format(eB)
    print "Decryption key A:", '{0:,}'.format(dA)
    print "Decryption key B:", '{0:,}'.format(dB)

    (header, body) = utils.splitToHeaderBody(filename_ori)
    body = utils.padding(body, dim_blocco)
    utils.writePadding(filename_pad, header, body)
    body_list = utils.chunkBody(body, dim_blocco)
    body1AtoB = utils.char2int(body_list, p)

    print "A -encrypt-> B"
    body1AtoB = utils.algorithm(body1AtoB, eA, p)
    utils.writeFileDec(filename + "_eA." + fileext, header, body1AtoB, dim_blocco)

    print "B -encrypt-> A"
    body1BtoA = utils.algorithm(body1AtoB, eB, p)
    utils.writeFileDec(filename + "_eB." + fileext, header, body1BtoA, dim_blocco)

    print "A -decrypt-> B"
    body2AtoB = utils.algorithm(body1BtoA, dA, p)
    utils.writeFileDec(filename + "_dA." + fileext, header, body2AtoB, dim_blocco)

    print "B -decrypt-> A"
    body2BtoA = utils.algorithm(body2AtoB, dB, p)
    utils.writeFile(filename_dec, header, body2BtoA)

    if utils.md5same(utils.md5(filename_pad), utils.md5(filename_dec)):
        print "File decodificato correttamente"
    else:
        print "Il file decodificato e' diverso dall'originale'"

    print "Tempo impiegato:", round(time.time() - tstart, 2), "secondi"
