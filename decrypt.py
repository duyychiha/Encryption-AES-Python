#!/usr/bin/python
# coding=utf-8
# decrypt.py –m <mode <infile> <outfile>

#Module co ban
import sys, getopt, struct
#Module PyCrypto
from Crypto.Cipher import AES
#Module ham bam hash
import hashlib

#Key set mac dinh cho chuong trinh
#Gia du 2 ben deu da biet key nay
MyKey = "8765432112345678" * 2
BlockSize = 16 * 64 * 1024 # = 1024*1024, block size phai chia het cho 16!!

#=======================Ham Decrypt=================================
def decrypt(mode, input_name, output_name):
	if mode != "ECB" and mode != "CBC" and mode != "CFB" and mode != "OFB" and mode != "CTR":
		print "Available modes: ECB, CBC, CFB, OFB, CTR...."
		print "Plz choose again!"
		sys.exit()

	if(mode == "ECB"):
		mode = AES.MODE_ECB
	elif (mode == "CFB"):
		mode = AES.MODE_CFB
	elif (mode == "OFB"):
		mode = AES.MODE_OFB
	elif (mode == "CTR"):
		mode = AES.MODE_CTR
	elif (mode == "CBC"):
		mode =  AES.MODE_CBC
	else:
		#Mac dinh la mode CBC
		print "Wrong mode! Set CBC as default mode!!"
		mode = AES.MODE_CBC

	#Tao key 32bit bang ham bam tu key dinh san
	key = hashlib.sha256(MyKey).digest()	#sha256 cho ra 32bytes key

	with open(input_name, "rb") as f_in:
		size = struct.unpack('<Q',f_in.read(struct.calcsize('Q')))[0]
		IV = f_in.read(16)		#read 16 thoi vi IV xai hash MD5
		decryptor = AES.new(key, mode, IV)

		with open(output_name, "wb") as f_out:
			while True:
				block = f_in.read(BlockSize)
				if len(block) == 0:
					break
				content = decryptor.decrypt(block)
				#print content
				f_out.write(content)
			f_out.truncate(size)	#Xoa padding, cho ve dung size goc
	return
#================================================================


#=======================Ham Main=================================
def main(argv):
	#XU ly tham so dong lenh
	#print "Number of arguments:", len(sys.argv), "argument."
	#print "Argument List:", str(sys.argv)

	try:
		#getopt.getopt(args, options, [long_options])
		opts, args = getopt.getopt(argv,"hm:")
	except getopt.GetoptError:
		print "decrypt.py –m <mode <infile> <outfile>"
		sys.exit(2)

	#Neu danh sach tham so sau khi tru di cac option
	#khong phai la dang: "encrypt.py <input_file> <output_file>
	if( len(args) != 3 and len(args) != 2):
		#print "Invalid Arguments!"
		print "decrypt.py –m <mode <infile> <outfile>"
		sys.exit(2)

	#Lay thong tin input_file va output_file
	input_file = args[0]
	if(len(args) == 2):
		output_file = args[1]
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

	#Goi ham decrypt
	decrypt(mode,input_file,output_file)
	return
#=================================================================

if __name__ == "__main__":
	main(sys.argv[1:])
