#!/usr/bin/python
# coding=utf-8
# very_sign.py -h <hash> <fileinput> <ten_file_chua_chu_ky>

#Module co ban
import sys, getopt, os
#Module PyCrypto, Hash
from Crypto.Hash import SHA256, MD5, SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto import Random

BlockSize = 16 * 64 * 1024 # = 1024*1024, block size phai chia het cho 16!!

# sign.py -h <hash> <fileinput> <ten_file_se_ghi_chu_ky>

def very_sign(hash,input_name,sign_file):

    #--------------Chon loai Hash-------------------
    print "Hash mode:", hash
    if hash != "SHA256" and hash != "MD5" and hash != "SHA" and hash != "SHA1" and hash != "SHA-1":
        print "Supported modes: SHA256, MD5, SHA."
        print "Plz choose again!"
        sys.exit()

    if(hash == "SHA256"):
        hash = SHA256
    elif (hash == "MD5"):
        hash = MD5
    elif (hash == "SHA" or hash == "SHA1" or hash == "SHA-1"):
        hash = SHA
    #print "Hash mode: ", hash


    #-----Bam noi dung file input (lam giong cau 3 checksum)
    # Tao Object MyHash thuoc lop checksum do thong so dua vao
    MyHash = hash.new()

    #Doc noi dung file input
    with open(input_name,"rb") as f_in:
        while True:
            block = f_in.read(BlockSize)
            if len (block) == 0:
                break
            MyHash.update(block)

    hash = MyHash
    #if(hash == SHA or hash == MD5):
        #hash = MyHash.digest()
    #elif (hash == SHA256):
        #hash = MyHash.hexdigest()

    #Doc signature
    with open(sign_file,"rb") as f_in2:
        signature = f_in2.read()
    print "Signature get:", signature

    #Doc public key
    if os.path.isfile("public.key"):
        with open("public.key","r") as f_in:
            public_key = RSA.importKey(f_in.read())
    else:
        print "Pubkey doesn't exist... Task failed.....!!"
        return False

    check = PKCS1_v1_5.new(public_key)
    result = check.verify(hash,signature)
    print "Verify check:", result
    return result

#=======================Ham Main=================================
def main(argv):
    #XU ly tham so dong lenh
    #print "Number of arguments:", len(sys.argv), "argument."
    #print "Argument List:", str(sys.argv)

    try:
        #getopt.getopt(args, options, [long_options])
		opts, args = getopt.getopt(argv,"h:")
    except getopt.GetoptError:
        print "very_sign.py -h <hash> <fileinput> <ten_file_chua_chu_ky>"
        sys.exit(2)

    #Chay vong for de lay option
    for opt, arg in opts:
        if opt == "-h":
            hash = arg.upper()

    #Neu danh sach tham so sau khi tru di cac option
    #khong phai la dang: "<input_file>
    #print args
    if(len(args) != 2):
        #print "Invalid Arguments!"
        #print args
        print "Missing inputfile name!!"
        print "very_sign.py -h <hash> <fileinput> <ten_file_chua_chu_ky>"
        sys.exit(2)

    #Lay thong tin input_file va output_file
    input_file = args[0]
    file_signed = args[1]
    #---------------Xu ly xong tham so dong lenh-------------------

	#Goi ham checksum
    tmp = very_sign(hash,input_file,file_signed)
    print "Verify result:", tmp
    return tmp

#=================================================================

if __name__ == "__main__":
    main(sys.argv[1:])
