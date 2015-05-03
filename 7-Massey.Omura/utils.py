import hashlib
from fractions import gcd
import sys
import pyprimes

def md5same(md5_1, md5_2):
    if md5_1 == md5_2:
        print "Yeah, i due file sono uguali"
    else:
        sys.exit("Ops, i due file non sono uguali -> EXIT")
    
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


if __name__ == "__main__":
    print modinv(43, 103)
    print next(pyprimes.primes_above(100000000))
