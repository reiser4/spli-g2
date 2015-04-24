import hashlib


def md5same(md5_1, md5_2):
    if md5_1 == md5_2:
        print "Yeah, i due file sono uguali"
    else:
        print "Ops, i due file non sono uguali -> EXIT"
        sys.exit()
    
def md5(filename):
    return hashlib.md5(open(filename, 'rb').read()).hexdigest()

