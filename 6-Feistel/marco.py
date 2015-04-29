import sys
import os
from random import randrange
import utils
import feistel


"""
def max_codifica( key , block ):

def max_decodifica( key , block):

"""

def create_crypted_file(chiave, filename):

	## prendi un parametro della funzione e poi lo sovrascrivi??
	#filename = sys.argv[1]
	dim_blocco = 4
	symbol_padding = '0'
	len_header = 18
	
	print 'Opening '+filename+'...'
	file = open(filename,'r')
	data = file.read()
	file.close()

	print "Size : "+ str(len(data)) + " byte"

	module = len(data) % dim_blocco
	padding = dim_blocco - module
	
	if padding > 0:
		data = data.ljust(len(data)+padding,symbol_padding); 
		print "Padding of "+str(padding)+"byte added!"

		newfile = open("file-padded.tga", 'wb')
		newfile.write(data)
		newfile.flush()
		newfile.close()

		print "Created file-padded.tga. "

	header = data[0:len_header]
	body = data[len_header:]

	blockList = []

	numBlocks = len(body)/dim_blocco
	print "Number of blocks :" + str(numBlocks)

	print "Creating block list.."
	for i in range (0,numBlocks):
		
		a = dim_blocco*i
		b = dim_blocco*i + dim_blocco
		blockList.append(body[a:b])

	print "List composed of "+str(numBlocks)+" blocks created."

	for i in range(0,numBlocks):
		blockList[i] =  feistel.crypt(chiave , blockList[i])

	newCryptedfile = open("file-crypted.tga", 'wb')

	print "Writing header...."
	newCryptedfile.write(header)

	print "Writing crypted blocks on file.."
	for i in range(0,numBlocks):
		#blockList[i] =  max_codifica(chiave , blockList[i])
		newCryptedfile.write(blockList[i])
	newCryptedfile.flush()
	newCryptedfile.close()
	print "Cryption ok. file saved."

	filename = "file-crypted.tga"
	return filename 
	
def create_decrypted_file(key , filename):

	#filename = sys.argv[1]
	dim_blocco = 4
	len_header = 18
	print 'Opening '+filename+'...'
	file = open(filename,'r')
	data = file.read()
	file.close()

	blockList = []
	header = data[0:len_header]
	body = data[len_header:]

	numBlocks = len(body)/dim_blocco
	print "Number of blocks :" + str(numBlocks)

	print "Creating block list.."
	for i in range (0,numBlocks):
		
		a = dim_blocco*i
		b = dim_blocco*i + dim_blocco
		blockList.append(body[a:b])

	for i in range(0,numBlocks):
		blockList[i] =  feistel.decrypt(key , blockList[i])

	newDeCryptedfile = open("file-decrypted.tga", 'wb')

	print "Writing header..."
	newDeCryptedfile.write(header)

	print "Writing decrypted blocks on file.."
	for i in range(0,numBlocks):
		#blockList[i] =  max_codifica(chiave , blockList[i])
		newDeCryptedfile.write(blockList[i])
	newDeCryptedfile.flush()
	newDeCryptedfile.close()
	print "Decryption ok. file saved."

	filename = "file-decrypted.tga"
	return filename



if sys.argv[1] == "encrypt":
	create_crypted_file(sys.argv[2], sys.argv[3])

if sys.argv[1] == "decrypt":
	create_decrypted_file(sys.argv[2], sys.argv[3])