#!/usr/bin/python
# coding=utf-8
#encrypt.py –m <mode> –i <IV> <input_file> <output_file>

#Module co ban
import sys, getopt, os, struct
#Module PyCrypto
from Crypto.Cipher import AES
#Module ham bam hash
from Crypto.Hash import MD5, SHA256
import  Crypto.Util.Counter

#encrypt.py –m <mode> –i <IV> <input_file> <output_file>

#Key set mac dinh cho chuong trinh
#Gia du 2 ben deu da biet key nay
MyKey = "8765432112345678" * 2
BlockSize = 16 * 64 * 1024 # = 1024*1024, block size phai chia het cho 16!!
Padding = "@"

#ctr = Crypto.Util.Counter.new(128, initial_value=long(iv.encode("hex"), 16))

#cipher = Crypto.Cipher.AES.new(key, Crypto.Cipher.AES.MODE_CTR, counter=ctr)
#print cipher.encrypt(plaintext)

#=======================Ham Encrypt=================================
def encrypt(mode, IV, input_name, output_name):

	if mode != "ECB" and mode != "CBC" and mode != "CFB" and mode != "OFB" and mode != "CTR":
		print "Available modes: ECB, CBC, CFB, OFB, CTR."
		print "Plz choose again!"
		sys.exit()

	if(mode == "ECB"):
		mode = AES.MODE_ECB
	elif (mode == "CFB"):
		mode = AES.MODE_CFB
	elif (mode == "OFB"):
		mode = AES.MODE_OFB
	elif (mode == "CBC"):
		mode =  AES.MODE_CBC
	elif (mode == "CTR"):
		mode = AES.MODE_CTR

	#Tao key 32bit bang ham bam tu key dinh san
	MyHash = SHA256.new(MyKey)
	key = MyHash.digest()
	#print "Size: ", key
	#key = hashlib.sha256(MyKey).digest()	#sha256 cho ra 32bytes key
	#Bam lai IV cho chuan
	MyHash = MD5.new(IV)
	IV = MyHash.digest()
	#IV = hashlib.md5(IV).digest()			#MD5 hash cho ra 16bytes


	if (mode != AES.MODE_CTR):
		encryptor = AES.new(key, mode, IV)
	else:
		ctr = Crypto.Util.Counter.new(128, initial_value=long(IV.encode("hex"), 16))
		encryptor = AES.new(key, AES.MODE_CTR, counter=ctr)

	filesize = os.path.getsize(input_name)
	print "File size: ", filesize
	#Bat dau doc va ghi file
	with open(input_name, "rb") as f_in:
		with open(output_name,"wb") as f_out:
			#Ghi file size ra
			# "<": Little Edian, "Q": unsigned long long
			f_out.write(struct.pack('<Q',filesize))
			f_out.write(IV)		#IV dai 16 byte do hash MD5

			#while - do: doc ghi file theo block size
			while True:
				block = f_in.read(BlockSize)
				#print "Block:", block
				if len(block) == 0:
					break
				elif len(block) % 16 != 0:
					#Padding cho du block
					block = block + Padding * (16 - len(block) % 16)
					#print "Block with pads:", block
				f_out.write(encryptor.encrypt(block))
	return
#================================================================


#=======================Ham Main=================================
def main(argv):
	#XU ly tham so dong lenh
	#print "Number of arguments:", len(sys.argv), "argument."
	#print "Argument List:", str(sys.argv)

	try:
		#getopt.getopt(args, options, [long_options])
		opts, args = getopt.getopt(argv,"hm:i:")
	except getopt.GetoptError:
		print "encrypt.py –m <mode> –i <IV> <input_file> <output_file>"
		sys.exit(2)

	#print "ARGS:", args
	#Neu danh sach tham so sau khi tru di cac option
	#khong phai la dang: "encrypt.py <input_file> <output_file>
	if( len(args) != 3 and len(args) != 2):
		#print "Invalid Arguments!"
		print "Type as: encrypt.py –m <mode> –i <IV> <input_file> <output_file>"
		sys.exit(2)

	#Lay thong tin input_file va output_file
	input_file = args[0]
	if(len(args) == 2):
		output_file = args[1]
	else:
		#Neu khong co thong so output thi mac dinh la ten fileinput.enc
		output_file = input_file + ".enc"

	#Chay vong for de lay option
	for opt, arg in opts:
		if opt == "-h":
			print "encrypt.py -m <mode> -i <IV> <input_file> <output_file>"
			sys.exit()
		elif opt == "-m":
			mode = arg.upper()
		elif opt == "-i":
			IV = arg
	#---------------Xu ly xong tham so dong lenh-------------------

	#Goi ham ENCRYPT
	encrypt(mode, IV, input_file, output_file)

	return
#=================================================================

if __name__ == "__main__":
	main(sys.argv[1:])
