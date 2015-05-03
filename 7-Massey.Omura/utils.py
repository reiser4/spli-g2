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
    return next(pyprimes.primes_above(n))
    
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

if __name__ == "__main__":
    print modinv(43, 103)
    print next(pyprimes.primes_above(100000000))
