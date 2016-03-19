#!/usr/bin/python
# coding=utf-8
# decrypt.py –m <mode <infile> <outfile>

#Module co ban
import sys, getopt, os, struct
#Module PyCrypto
from Crypto.Cipher import AES
#Module ham bam hash
import hashlib


def encrypt(mode, IV, input_name, output_name):
	if mode != "ECB" and mode != "CBC" and mode != "CFB" and mode != "OFB" and mode != "CTR":
		print "Available modes: ECB, CBC, CFB, OFB, CTR...."
		sys.exit()

	if(mode == "ECB"):
		mode = AES.MODE_ECB
	elif (mode == "CFB"):
		mode = AES.MODE_CFB
	elif (mode == "OFB"):
		mode = AES.MODE_OFB
	elif (mode == "CTR"):
		mode = AES.MODE_CTR
	else:
		#Mac dinh la mode CBC
		mode = AES.MODE_CBC

	with open(input_name, "rb") as f_in:
        size = struct.unpack("<Q",infile.read(struct,calcsize("Q")))
        IV = infile.read(32)
        decryptor = AES.new(key, mode, IV)
        with open(output_name, "wb") as f_out:



	return


def main(argv):
	#XU ly tham so dong lenh
	print "Number of arguments:", len(sys.argv), "argument."
	print "Argument List:", str(sys.argv)

	#Kiem tra noi dung module AES
	#content = dir(AES)
	#print content

	try:
		#getopt.getopt(args, options, [long_options])
		opts, args = getopt.getopt(argv,"hm:")
	except getopt.GetoptError:
		print "decrypt.py –m <mode <infile> <outfile>"
		sys.exit(2)

	#Neu danh sach tham so sau khi tru di cac option
	#khong phai la dang: "encrypt.py <input_file> <output_file>
	if( len(args) != 3 and len(args) != 2):
		print "Invalid Arguments!"
		print "decrypt.py –m <mode <infile> <outfile>"
		sys.exit(2)

	#Lay thong tin input_file va output_file
	input_file = args[1]
	if(len(args) == 3):
		output_file = args[2]
	else:
		#Neu khong co thong so output thi mac dinh la ten fileinput.enc
		output_file = input_file + ".dec"

	#Chay vong for de lay option
	for opt, arg in opts:
		if opt == "-h":
			print "decrypt.py –m <mode <infile> <outfile>"
			sys.exit()
		elif opt == "-m":
			mode = arg.upper()
	#---------------Xu ly xong tham so dong lenh-------------------

if __name__ == "__main__":
	main(sys.argv[1:])
