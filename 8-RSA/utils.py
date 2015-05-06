import hashlib
import fractions
import sys
import pyprimes

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
    
def calculateEncryptionKey(nthprime, fp):
    """
    Prende in ingresso la posizione del numero primo che si vuole calcolare (se passo 10, prendo il decimo numero primo) e 'p'
    restituisce 'e' ovvero un numero primo diverso da p-1 e che sia primo con quest'ultimo
    """
    e = pyprimes.nth_prime(nthprime)
    #fp = p-1
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

def writeFileTmp(filename, header, body):
    """
    Il body deve essere una lista di interi perche' per ogni ciclo trasformo
    l'intero in carattere, questo per evitare un ulteriore ciclo for'
    """
    #body = int2char(body)
    fileout = open(filename,'wb')
    fileout.write(header)
    for b in body:
        fileout.write(chr(b%256))
    fileout.flush()
    fileout.close()
    
    fileoutint = open(filename + "-int",'wb')
    for b in body:
        fileoutint.write(str(b) + " ")
    fileoutint.flush()
    fileoutint.close()

def writeFile(filename, header, body):
    """
    Il body deve essere una lista di interi perche' per ogni ciclo trasformo
    l'intero in carattere, questo per evitare un ulteriore ciclo for'
    """
    #body = int2char(body)
    fileout = open(filename,'wb')
    fileout.write(header)
    for b in body:
        fileout.write(chr(b))
    fileout.flush()
    fileout.close()

def int2char(intlist):
    tmp = list()
    for i in intlist:
        tmp.append(chr(i))
    return tmp

def char2int(charlist, p):
    tmp = list()
    for c in charlist:
        res = ord(c)
        if res > p:
            sys.exit("L'intero:", c, "e' maggiore della chiave p:", p, ", aumentare la chiave'")
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


