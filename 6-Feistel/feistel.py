 # coding=utf-8
import hashlib

def funzione(key, IN):
    m = hashlib.sha1() # Inizializzo SHA1
    res = IN ^ key # IN xor Key
    res = hex(res)[2:].zfill(4) 
    m.update(res) # SHA1(IN + key) --> output
    res = m.hexdigest()[:4] # Tronco i 2 byte = 16 bit
    res = int(res,16)
    return res
    

def char2hex(char_type):   
    res = 0
    for i in char_type:
        res <<= 8
        res += ord(i)
    
    return res

def hex2char(hex_type):
    
    l = list()
    while hex_type != 0:
        l.append(hex_type &0xff)
        hex_type >>= 8
        
    l.reverse()
    
    stringa = ''
    for i in l:
        stringa += chr(i)
        
    
    return stringa
    
def cod(block, key):
    # Ricevo blocco block di 32 bit
    #0               16              32
    #+----------------+---------------+
    #|       L_i      |     R_i       |
    #+----------------+---------------+
    #                         |
    #                         V
    #                   +---------------+
    #                   | SHA1(R_i + K) |
    #       R_i         +---------------+  
    #        |                 |
    #        |           L_i---+
    #        V                 |
    #+----------------+---------------+
    #|       L_i+1    |     R_i+1     |
    #+----------------+---------------+
    #
    # Divido il blocco da 32 bit in due da da 16bit L_i R_i
    # restituisco [R_i, SHA1(R_i + K) + L_i]
    #
    # Traduco il blocco stringa in un intero Ex: ROMA ==> 0x524f4d41
    block = char2hex(block)
    # Divido in due il blocco Ex: 0x524f4d41 ==> Li = 0x524f Ri=4d41
    Li = (int(block) & 0xffff0000) >> 16 # 16 bit più significativi sono L_i
    Ri = int(block) & 0x0000ffff # 16 bit meno significativi sono R_i
    
    Ri1 = Li ^ funzione(key,Ri)
    Li1 = Ri
    Li1 = hex2char(Li1)
    Ri1 = hex2char(Ri1)
    return Li1 + Ri1
        
    
def decod(block, key):
    
    block = char2hex(block)
    Li1 = (int(block) & 0xffff0000) >> 16 # 16 bit più significativi sono L_i
    Ri1 = int(block) & 0x0000ffff # 16 bit meno significativi sono R_i
    
    Li = funzione(key,Li1) ^ Ri1
    Ri = Li1
    
    Li = hex2char(Li)
    Ri = hex2char(Ri)
    return Li + Ri
    
    
    
    
def main():
    
    key = 7
    
    INPUT = "ROMA"
    print "INPUT =", INPUT
    OUTPUT = cod(INPUT,key)
    print "OUTPUT =", OUTPUT
    print decod(OUTPUT,key)
    
if __name__ == "__main__":
        main()
