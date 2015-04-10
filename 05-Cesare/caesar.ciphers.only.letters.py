import os.path
import sys

MAX_KEY_SIZE = 26


def caesarCiphers(mode, key, file_input, file_output):
	finput = open(file_input, 'r')
	if mode[0] == 'b':
		foutput = open(file_output, 'a')
	else:
		foutput = open(file_output, 'w')
	
	message = finput.read()
	finput.close()
    
	if mode[0] == 'd':
		key = -key
	
	translated = ''

	for symbol in message:
		if symbol.isalpha():
			num = ord(symbol)
			num += key

			if symbol.isupper():
				if num > ord('Z'):
					num -= 26
				elif num < ord('A'):
					num += 26
			elif symbol.islower():
				if num > ord('z'):
					num -= 26
				elif num < ord('a'):
					num += 26

			translated += chr(num)
		else:
			translated += symbol
	
	translated += '\n'
	
	foutput.write(translated)
	foutput.flush()
	foutput.close()

def encrypt(file, key, file_encrypt):
	print "Start encrypt"
	caesarCiphers("e", key, file, file_encrypt)
	print "Encrypt done"

def decrypt(file_encrypt, key, file_decript):
	print "Start decrypt"
	caesarCiphers("d", key, file_encrypt, file_decrypt)
	print "Decrypt done"

def bruteforce(file_encrypt, file_bruteforce):
	print "Start brute force"
	for key in range(1, MAX_KEY_SIZE + 1):
		caesarCiphers("b", key, file_encrypt, file_bruteforce)
	print "Brute force done"


if __name__ == "__main__":
		
	if len(sys.argv) != 3:
		print "ERROR: 'python caesar.ciphers.only.letters.py file_name.txt chiave'"
		sys.exit(0)
	
	file = sys.argv[1]
	key = int(sys.argv[2])
	
	print "Nome file: " + file
	print "Chiave: " + str(key)
	print ""
	
	if not os.path.isfile(file):
		print "\nERROR: il file non esiste"
		sys.exit(0)
		
	file_split = file.split(".")
		
	file_name = file_split[0]
	file_ext = file_split[1]
	if file_ext != "txt":
		print "Error: the name of file is wrong"
		sys.exit(0)

	file_encrypt = file_name + "_encrypt.txt" 
	file_decrypt = file_name + "_decrypt.txt"
	file_bruteforce = file_name + "_bruteforce.txt"
	
	if os.path.isfile(file_bruteforce):
		os.remove(file_bruteforce)
	
	encrypt(file, key, file_encrypt)
	decrypt(file_encrypt, key, file_decrypt)
	bruteforce(file_encrypt, file_bruteforce)
	