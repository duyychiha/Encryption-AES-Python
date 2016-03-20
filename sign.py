#!/usr/bin/python
# coding=utf-8
# sign.py -h <hash> <fileinput> <ten_file_se_ghi_chu_ky>

#Module co ban
import sys, getopt
#Module PyCrypto, Hash
from Crypto.Hash import SHA256, MD5, SHA
from Crypto.PublicKey import RSA
from Crypto import Random

BlockSize = 16 * 64 * 1024 # = 1024*1024, block size phai chia het cho 16!!

# sign.py -h <hash> <fileinput> <ten_file_se_ghi_chu_ky>
def sign(hash,input_name,file_signed):
    key = RSA.generate(1024)
    hash = SHA256.new("123456").digest()
    signature = key.sign(hash,"")
    return

#=======================Ham Main=================================
def main(argv):
    #XU ly tham so dong lenh
    print "Number of arguments:", len(sys.argv), "argument."
    print "Argument List:", str(sys.argv)

    try:
        #getopt.getopt(args, options, [long_options])
		opts, args = getopt.getopt(argv,"h:")
    except getopt.GetoptError:
        print "sign.py -h <hash> <fileinput> <ten_file_se_ghi_chu_ky>"
        sys.exit(2)

    # checksum.py -h <hash> -c <checksum> <inputfile>
    #Chay vong for de lay option
    # check_checksum = False (ko co option -c thi
    # se tao check sum va xuat ra output chuan.
    # Neu check_checksum = True thi se kiem tra checksum co khop hay ko?
    mychecksum = None
    for opt, arg in opts:
        if opt == "-h":
            hash = arg

    #Neu danh sach tham so sau khi tru di cac option
    #khong phai la dang: "<input_file>
    #print args
    if(len(args) != 2):
        #print "Invalid Arguments!"
        print args
        print "Missing inputfile name!!"
        print "sign.py -h <hash> <fileinput> <ten_file_se_ghi_chu_ky>>"
        sys.exit(2)

    #Lay thong tin input_file va output_file
    input_file = args[0]
    file_signed = args[1]
    #---------------Xu ly xong tham so dong lenh-------------------

	#Goi ham checksum
    tmp = sign(hash,input_file,file_signed)

#=================================================================

if __name__ == "__main__":
    main(sys.argv[1:])
