import utils
import pyprimes
import fractions
import sys
import marco
import feistel

if __name__ == "__main__":
    iA = 100
    iB = 101
    p = utils.calculateP(100000)
    fp = p-1
    
    eA = utils.calculateEncryptionKey(100, p)
    eB = utils.calculateEncryptionKey(101, p)
    dA = utils.modinv(eA, fp)
    dB = utils.modinv(eB, fp)
    
    (header, body) = marco.create_crypted_file(eA, "lena.tga")
    body1 = list()
    for b in body:
        b = str(b)
        res = b.encode('hex')
        res = int(res,16)
        body.append(pow(res, eA, p))
    
    f_body1 = open("lena1.tga", 'wb')
    f_body1.write(header)
    for b in body1:
        #blockList[i] =  max_codifica(chiave , blockList[i])
        res = hex(b)[2:]
        f_body1.write(res)
    f_body1.flush()
    f_body1.close()
    
    print eA, eB, dA, dB
    m = 14646
    print m
    m1 = pow(m, eA, p)
    print m1
    m2 = pow(m1, eB, p)
    print m2
    m3 = pow(m2, dA, p)
    print m3
    m4 = pow(m3, dB, p)
    print m4
