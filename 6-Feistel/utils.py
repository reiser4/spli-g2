import hashlib

def md5same(md5_1, md5_2):
    if md5_1 == md5_2:
        #print "Yeah, i due file sono uguali"
        return True
    else:
        #print "Ops, i due file non sono uguali -> ritenta, sarai piu' fortunato"
        return False
    
def md5(filename):
    return hashlib.md5(open(filename, 'rb').read()).hexdigest()

