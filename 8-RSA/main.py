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
    
    dim_blocco = 4
    
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
    print "N:", n
    print "Encryption key A:", '{0:,}'.format(e)
    #print "Encryption key B:", '{0:,}'.format(eB)
    print "Decryption key A:", '{0:,}'.format(d)
    #print "Decryption key B:", '{0:,}'.format(dB)

    (header, body) = utils.splitToHeaderBody(filename_ori)
    
    body = utils.padding(body, dim_blocco)
    
    utils.writePadding("file-paddato.tga",header,body)
    
    body_list = utils.chunkBody(body, dim_blocco)
    
    
    #TODO: Fare Padding (Del body)
    #TODO: Salvare l'immagine paddata
    #TODO: Dividere in blocchi il body
    #TODO: Ora blocchi e' una stringa di ascii 
    #      e' meglio trasformare i blocchi nel loro corrispettivo intero 
    
    body_num = utils.char2int(body_list, n) #TODO: Questo verra' cancellato

    # Inizio Cifratura
    print "A encrypt"
    body1AtoB = utils.algorithm(body_num, e, n) # Qui passiamo la lista di blocchi
    print len(body1AtoB)                                            # gia'' trasformata in interi
    utils.writeFileTmp(filename + "_eA." + fileext, header, body1AtoB)
    
    #print "B -encrypt-> A"
    #body1BtoA = utils.algorithm(body1AtoB, eB, p)
    #utils.writeFileTmp(filename + "_eB." + fileext, header, body1BtoA)
    
    print "B decrypt"
    body2AtoB = utils.algorithm(body1AtoB, d, n)
    print len(body2AtoB)
    utils.writeFile(filename + "_dA." + fileext, header, body2AtoB)
    
    #print "B -decrypt-> A"
    #body2BtoA = utils.algorithm(body2AtoB, dB, p)
    #utils.writeFile(filename_dec, header, body2BtoA)
    
    if utils.md5same(utils.md5("file-paddato.tga"), utils.md5(filename + "_dA." + fileext)):
        print "File decodificato correttamente"
    else:
        print "Il file decodificato e' diverso dall'originale'"

    print "Tempo impiegato:", round(time.time() - tstart, 2), "secondi"
