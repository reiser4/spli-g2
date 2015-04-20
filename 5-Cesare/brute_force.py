# Attacco a Dizionario
from string import ascii_lowercase

def caesar(word, key):
    enc = ''
    for letter in word:
        enc= enc + ascii_lowercase[(ascii_lowercase.find(letter)+key)%len(ascii_lowercase)]
        
    return enc

def find_key(file_to_crack):

    #Apro il dizionario

    l_min = 3
    word_max = 100

    diz = open('wordsEn.txt','rU')
    enc = open(file_to_crack,'rU')

    word_in_enc = list()
    word_in_diz = list()

    for word in diz:
        if len(word[:-1]) > l_min:
            word_in_diz.append(word[:-1])

    # Usare le prime word_max parole diverse

    while len(word_in_enc)<=word_max:
        line = enc.readline()
        line = line[:-1]
        line = line.split()
        for word in line:
            if (word not in word_in_enc) and len(word) > l_min:
                word_in_enc.append(word)
        
                 
    occorrenze = list()

    for i in range(len(ascii_lowercase)):
        occorrenze.append(0)


    for key in range(1,len(ascii_lowercase)):
        for word in word_in_enc:
            if caesar(word,key) in word_in_diz:
                occorrenze[key-1] +=1
            
        print occorrenze
        
    key = len(ascii_lowercase)- (occorrenze.index(max(occorrenze)) + 1)
    return key
