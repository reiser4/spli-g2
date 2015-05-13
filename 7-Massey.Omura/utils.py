import hashlib
import fractions
import sys
import pyprimes
import binascii

def md5same(md5_1, md5_2):
    if md5_1 == md5_2:
        #print "Yeah, i due file sono uguali"
        return True
    else:
        #sys.exit("Ops, i due file non sono uguali -> EXIT")
        return False

def md5(filename):
    return hashlib.md5(open(filename, 'rb').read()).hexdigest()

def egcd(a, b):
    # https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

def modinv(a, m):
    # https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m

def calculateP(n):
    """
    Prende in ingresso un numero 'n'
    restituisce il numero primo successivo a 'n'
    """
    return pyprimes.next_prime(n)

def calculateEncryptionKey(nthprime, p):
    """
    Prende in ingresso la posizione del numero primo che si vuole calcolare (se passo 10, prendo il decimo numero primo) e 'p'
    restituisce 'e' ovvero un numero primo diverso da p-1 e che sia primo con quest'ultimo
    """
    e = pyprimes.nth_prime(nthprime)
    fp = p-1
    while e == fp or fractions.gcd(e, fp) != 1:
        nthprime += 2
        e = pyprimes.nth_prime(nthprime)
    return e

def splitToHeaderBody(filename):
    lenheader = 18
    fileinput = open(filename,'rb')
    data = fileinput.read()
    fileinput.close()
    header = data[0:lenheader]
    body = data[lenheader:]
    return header, body

def writeFileDec(filename, header, body, dim_blocco):
    """
    Il body deve essere una lista di interi perche' per ogni ciclo trasformo
    l'intero in carattere, questo per evitare un ulteriore ciclo for'
    """
    fileout = open(filename,'wb')
    fileout.write(header)
    n_byte = 0
    for b in body:
        #fileout.write(chr(b%(256)))
        #print type(binascii.a2b_hex(b)), binascii.a2b_hex(b)
        b = b % pow(2,dim_blocco*8)
        #print b % pow(2,dim_blocco*8), " - " , b%256
        if hex(b)[-1] != 'L':
            res = hex(b)[2:]
        else:
            res = hex(b)[2:-1] # hex() mi riestitusce qualcosa che inizia con 0x e finisce con L
        if len(res) % 2 != 0:
            res = '0' + res
        #print "RES: ",res
        for i in range(len(res)/2):
            #print res[2*i:(2*i)+2], binascii.a2b_hex(res[2*i:(2*i)+2])
            fileout.write(binascii.a2b_hex(res[2*i:(2*i)+2]))
            n_byte += 1
    fileout.write("0"*2000)
    fileout.flush()
    fileout.close()
    #print "SCRITTI ", n_byte, "byte"

def writeFile(filename, header, body):
    """
    Il body deve essere una lista di interi perche' per ogni ciclo trasformo
    l'intero in carattere, questo per evitare un ulteriore ciclo for'
    """
    fileout = open(filename,'wb')
    fileout.write(header)
    n_byte = 0
    for b in body:
        if hex(b)[-1] != 'L':
            res = hex(b)[2:]
        else:
            res = hex(b)[2:-1] # hex() mi riestitusce qualcosa che inizia con 0x e finisce con L
        if len(res) % 2 != 0:
            res = '0' + res
        for i in range(len(res)/2):
            #print res[2*i:(2*i)+2], binascii.a2b_hex(res[2*i:(2*i)+2])
            fileout.write(binascii.a2b_hex(res[2*i:(2*i)+2]))
            n_byte += 1
    fileout.flush()
    fileout.close()
    #print "Scritti", n_byte, "byte"

def padding(body, dim_blocco):
    symbol_padding = '0'
    module = len(body) % dim_blocco
    padding = dim_blocco - module
    if padding > 0:
        body = body.ljust(len(body) + padding, symbol_padding)
    return body

def writePadding(filename, header, body):
    fileout = open(filename, 'wb')
    fileout.write(header)
    fileout.write(body)
    fileout.close()

def chunkBody(body, len_chunk):
    block_list = list()
    for i in range (len(body) / len_chunk):
        block_list.append(body[i*len_chunk:(i+1)*len_chunk])
    return block_list

def int2char(intlist):
    tmp = list()
    for i in intlist:
        tmp.append(chr(i))
    return tmp

def char2int(charlist, p):
    tmp = list()
    for word in charlist:
        res = binascii.b2a_hex(word)
        res = int(res,16)
        if res > p:
            sys.exit("ERRORE: L'intero: " + '{0:,}'.format(res) + " e' maggiore della chiave p: " + '{0:,}'.format(p) + ". Aumentare p")
        tmp.append(res)
    return tmp

def algorithm(message, k, p):
    tmp = list()
    for m in message:
        tmp.append(pow(m, k, p))
    return tmp

def phi(n):
    amount = 0
    for k in range(1, n + 1):
        if fractions.gcd(n, k) == 1:
            amount += 1
    return amount

if __name__ == "__main__":
    print modinv(43, 103)
    print pyprimes.next_prime(100000000)
