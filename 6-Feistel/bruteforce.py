import itertools
import utils
import time

if __name__ == "__main__":
    print "Welcome to the party\n" 
    print "Inizio l'attacco"
    start = time.time()
    for x in map(''.join, itertools.product('01', repeat=10)):
        # chiamo la funzione di Marco
        print "Calcolo l'md5 dei file per vedere se sono uguali"
        print "Attendi..."
        if md5same(md5('original_file'), md5('encrypt_file')):
            time = round(time.time() - start, 2)
            print "La chiave del tesoro e': " + str(x) + ", lunghezza " + str(len(x)) + " bit"
            print "E' stata trovata in: " + str(time) + " secondi"
            break
    print "\nJob done, goodbye"
