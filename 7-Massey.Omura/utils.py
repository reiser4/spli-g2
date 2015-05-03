import hashlib
from fractions import gcd
import sys

### gcd(20,8)

def md5same(md5_1, md5_2):
    if md5_1 == md5_2:
        print "Yeah, i due file sono uguali"
    else:
        sys.exit("Ops, i due file non sono uguali -> EXIT")
    
def md5(filename):
    return hashlib.md5(open(filename, 'rb').read()).hexdigest()

def findKeys(maxprime):
    numbers_prime = rwh_primes1(maxprime)
    p = numbers_prime[-1]
    da = 0
    db = 0
    i = 2
    y = 3
    while True: 
        da = gcd(numbers_prime[-i],p-1)
        if da == 1:
            ea = numbers_prime[-i]
            break
        i=+2
    while True:
        db = gcd(numbers_prime[-y],p-1)
        if db == 1:
            eb = numbers_prime[-y]
            break
        y+=2
    return ea, eb

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
