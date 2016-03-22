#!/usr/bin/python
# coding=utf-8
# sign.py -h <hash> <fileinput> <ten_file_se_ghi_chu_ky>

#Module co ban
import sys, getopt, os
#Module PyCrypto, Hash
from Crypto.Hash import SHA256, MD5, SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto import Random

BlockSize = 16 * 64 * 1024 # = 1024*1024, block size phai chia het cho 16!!

# sign.py -h <hash> <fileinput> <ten_file_se_ghi_chu_ky>

def sign(hash,input_name,file_signed):

    #--------------Chon loai Hash-------------------
    print "Hash mode:", hash
    if hash != "SHA256" and hash != "MD5" and hash != "SHA" and hash != "SHA1" and hash != "SHA-1":
        print "Supported modes: SHA256, MD5, SHA...."
        print "Plz choose again!"
        sys.exit()

    if(hash == "SHA256"):
        hash = SHA256
    elif (hash == "MD5"):
        hash = MD5
    elif (hash == "SHA" or hash == "SHA1" or hash == "SHA-1"):
        hash = SHA

    #Neu trong folder hien tai co private key thi se load len, ko thi
    # se tu tao private key
    if os.path.isfile("private_key.prv"):
        with open("private_key.prv","r") as f_in:
            key = RSA.importKey(f_in.read())
    else:
        #----------Tao RSA Key----------------
        MyRandom = Random.new().read
        key = RSA.generate(1024,MyRandom)

        #Luu private key lai
        with open("private_key.prv","w") as f_out:
            f_out.write(key.exportKey())


    #-----Bam noi dung file input (lam giong cau 3 checksum)
    # Tao Object MyHash thuoc lop checksum do thong so dua vao
    MyHash = hash.new()
    with open(input_name,"rb") as f_in:
        while True:
            block = f_in.read(BlockSize)
            if len (block) == 0:
                break
            MyHash.update(block)

    hash = MyHash

    #Sign bang private key
    MySign = PKCS1_v1_5.new(key)
    signature = MySign.sign(hash)

    #Ghi public key ra
    with open("public_key.pub","w") as f_out:
        f_out.write(key.publickey().exportKey())
        print "Public key:", key.publickey()

    #Ghi signature ra file
    with open(file_signed,"wb") as f_out:
        f_out.write(signature)
        print "Signature:", signature

    #print "Verify result:", RSA_Key.verify(hash,MySign)
    return MySign

#=======================Ham Main=================================
def main(argv):
    #XU ly tham so dong lenh

    try:
        opts, args = getopt.getopt(argv,"h:")
    except getopt.GetoptError:
        print "sign.py -h <hash> <fileinput> <ten_file_se_ghi_chu_ky>"
        sys.exit(2)

    #Chay vong for de lay option
    for opt, arg in opts:
        if opt == "-h":
            hash = arg.upper()

    #Neu danh sach tham so sau khi tru di cac option
    if(len(args) != 2):
        #print "Missing inputfile name!!"
        print "sign.py -h <hash> <fileinput> <ten_file_se_ghi_chu_ky>"
        sys.exit(2)

    #Lay thong tin input_file va output_file
    input_file = args[0]
    file_signed = args[1]
    #---------------Xu ly xong tham so dong lenh-------------------

	#Goi ham sign
    tmp = sign(hash,input_file,file_signed)
    return tmp

#=================================================================

if __name__ == "__main__":
    main(sys.argv[1:])
