#!/usr/bin/python
#encrypt.py –m <mode> –i <IV> <input_file> <output_file>

#Module co ban
import sys, getopt
#Module PyCrypto
from Crypto.Cipher import AES
#Module ham bam hash
import hashlib

def encrypt(mode, IV, input_name, output_name)
	if(mode != "ECB" && mode != "CBC" && mode != "CFB" && mode != "OFB" \
	&& mode != "CTR")
		print "Available modes: ECB, CBC, CFB, OFB, CTR...."
		sys.exit()

	if(mode == "ECB")
		mode = AES.MODE_ECB
	elif (mode == "CFB")
		mode = AES.MODE_CFB
	elif (mode == "OFB")
		mode = AES.MODE_OFB
	elif (mode == "CTR")
		mode = AES.MODE_CTR
	else
		mode = AES.MODE_CBC
		
	temp_key = "AKB49"
	#Tao key 32bit bang ham bam tu key dinh san
	key = hashlib.sha256(temp_key).digest()
	encryptor = AES.new(key, mode, IV)
	


def main(argv):
	#XU ly tham so dong lenh
	print "Number of arguments:", len(sys.argv), "argument."
	print "Argument List:", str(sys.argv)

	try:
		#getopt.getopt(args, options, [long_options])
		opts, args = getopt.getopt(argv,"hm:i:")
	expect getopt.GetoptError:
		print "encrypt.py –m <mode> –i <IV> <input_file> <output_file>"
		sys.exit(2)
	
	#Neu danh sach tham so sau khi tru di cac option
	#khong phai la dang: "encrypt.py <input_file> <output_file>
	if( len(args) != 3 and len(args) != 2)
		print "Invalid Arguments!"
		print "Type as: encrypt.py –m <mode> –i <IV> <input_file> <output_file>"
		sys.exit(2)
	
	#Lay thong tin input_file va output_file
	input_file = args[1]
	if(len(args) == 3)
		output_file = args[2]
	else
		#Neu khong co thong so output thi mac dinh la ten fileinput.enc
		output_file = input_file + ".enc"
	
	#Chay vong for de lay option
	for opt, arg in opts:
		if opt == "-h"
			print "encrypt.py -m <mode> -i <IV> <input_file> <output_file>"
			sys.exit()
		elif opt == "-m"
			mode = arg.upper()
		elif opt == "-i"
			IV = arg
	#---------------Xu ly xong tham so dong lenh-------------------

if __name__ == "__main__":
	main(sys.argv[1:])
