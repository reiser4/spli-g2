 # coding=utf-8
import hashlib
from random import randrange

def random_block(block_len):
    bit_len = 0 #Lunghezza attuale in bit del blocco
    block = ''
    while bit_len < block_len:
        block += chr(randrange(256))
        bit_len += 8
        
    return block 
    
def correlation_block( block_list ):
    copy_block = block_list[:]
    for i in range(1,len(block_list)):
        copy_block[i] = block_list[i] ^ block_list[i-1]
        #print block_list[i], block_list[i-1], copy_block[i]
        
    return copy_block
    
def decorrelation_block(block_list):
    
    for i in range(1,len(block_list)):
        #print block_list[i-1], block_list[i], block_list[i] ^ block_list[i-1]
        block_list[i] ^= block_list[i-1]
        
    return block_list
        

def funzione(key, IN):
    m = hashlib.sha1() # Inizializzo SHA1
    res = IN ^ key # IN xor Key
    res = hex(res)[2:].zfill(4) 
    #print res
    m.update(res) # SHA1(IN + key) --> output
    res = m.hexdigest()[:4] # Tronco i 2 byte = 16 bit
    #print m.hexdigest(), res
    res = int(res,16)
    #print "funzione restituisce %x" % res
    return res
    

def char2hex(char_type):   
    res = 0
    for i in char_type:
        res <<= 8
        res += ord(i)
        #print res, 
    #print "%x" % res
    return res

def hex2char(hex_type): # ERRORE
    
    l = list()
    #print "hex2char: ",
    while hex_type != 0:
        l.append(hex_type &0xff)
        #print "%x" % (hex_type &0xff),
        hex_type >>= 8
    while len(l) < 2:
        l.append(0)    
    l.reverse()
    #print l
    stringa = ''
    for i in l:
        stringa += chr(i)
      
    
    return stringa
    
def crypt(key, block):
    # Ricevo blocco block di 32 bit
    # Traduco il blocco stringa in un intero Ex: ROMA ==> 0x524f4d41
    block = char2hex(block)
    #block = block.encode('hex')
    key = int(key,2)
    #print key, block
    # Divido in due il blocco Ex: 0x524f4d41 ==> Li = 0x524f Ri=4d41
    Li = (int(block) & 0xffff0000) >> 16 # 16 bit più significativi sono L_i
    Ri = int(block) & 0x0000ffff # 16 bit meno significativi sono R_i
    
    Ri1 = Li ^ funzione(key,Ri)
    Li1 = Ri
    
    #print "Li1 %x Ri1 %x" % (Li1, Ri1)
    Li1 = hex2char(Li1).zfill(2)
    Ri1 = hex2char(Ri1).zfill(2)
    #Li1 = Li1.decode('hex')
    #Ri1 = Ri1.decode('hex')
    if len(Li1+Ri1) != 4:
        print "ERROR!"
    #print Li1, Ri1, Li1 + Ri1, len(Li1 + Ri1)
    #print "Li1 %s Ri1 %s" % (Li1, Ri1)
    #print "Li1 + Ri1 %s" % (Li1+Ri1)
    return Li1 + Ri1
        
    
def decrypt(key,block):
    
    block = char2hex(block)
    #print "block: %x" % block
    key = int(key,2)
    Li1 = (int(block) & 0xffff0000) >> 16 # 16 bit più significativi sono L_i
    Ri1 = int(block) & 0x0000ffff # 16 bit meno significativi sono R_i
    
    Li = funzione(key,Li1) ^ Ri1
    Ri = Li1
    
    Li = hex2char(Li).zfill(2)
    Ri = hex2char(Ri).zfill(2)
    #print "decr", Li.encode('hex'), Ri.encode('hex')
    return Li + Ri    
    
    
def main():
    
    key = "1010100110"
    debug = 0
    print random_block(32).encode('hex')
    
    prova = ''
    for i in range(4):
        prova += chr(0)
        
    print prova.encode('hex')
    
    block_list = [ char2hex(random_block(16)) for i in range(10) ]
    print block_list
    
    block_list = correlation_block(block_list)
    print block_list
    block_list = decorrelation_block(block_list)
    print block_list
    
    return 0
    if debug == 1:
        INPUT = "ROMA"
        
        print "INPUT =", INPUT
        OUTPUT = crypt(key,INPUT)
        print "OUTPUT =", OUTPUT, len(OUTPUT)
        print decrypt(key,OUTPUT)
    else:    
        a= "\x00\x00\x00\x00"
        
        print "INPUT =", INPUT.encode('hex')
        OUTPUT = crypt(key,INPUT)
        print "OUTPUT =", OUTPUT
        print decrypt(key,OUTPUT).encode('hex')
    
if __name__ == "__main__":
        main()
