#!/usr/bin/python
# coding=utf-8
# checksum.py -h <hash> -c <checksum> <inputfile>

#Module co ban
import sys, getopt
#Module PyCrypto, Hash
from Crypto.Hash import SHA256, MD5, SHA

BlockSize = 16 * 64 * 1024 # = 1024*1024, block size phai chia het cho 16!!

# checksum.py -h <hash> -c <checksum> <inputfile>
# Neu checksum != null thi kiem tra, ko thi tao checksum
def check_sum(hash, checksum, input_name):

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
    print "Hash mode: ", hash

    # Tao Object MyHash thuoc lop checksum do thong so dua vao
    MyHash = hash.new()

    with open(input_name,"rb") as f_in:
        while True:
            block = f_in.read(BlockSize)
            if len (block) == 0:
                break
            MyHash.update(block)

        if(checksum != None):
            return checksum == MyHash.hexdigest()
        else:
            return MyHash.hexdigest()


#=======================Ham Main=================================
def main(argv):
    #XU ly tham so dong lenh
    print "Number of arguments:", len(sys.argv), "argument."
    print "Argument List:", str(sys.argv)

    try:
        #getopt.getopt(args, options, [long_options])
		opts, args = getopt.getopt(argv,"h:c:")
    except getopt.GetoptError:
        print "checksum.py -h <hash> -c <checksum> <inputfile>"
        sys.exit(2)

    # checksum.py -h <hash> -c <checksum> <inputfile>
    #Chay vong for de lay option
    # check_checksum = False (ko co option -c thi
    # se tao check sum va xuat ra output chuan.
    # Neu check_checksum = True thi se kiem tra checksum co khop hay ko?
    mychecksum = None
    for opt, arg in opts:
        if opt == "-h":
            hash = arg.upper()
        elif opt in ("-c"):
            print "Checksum: ", arg
            mychecksum = arg

    #Neu danh sach tham so sau khi tru di cac option
    #khong phai la dang: "<input_file>
    #print args
    if(len(args) != 1):
        #print "Invalid Arguments!"
        print args
        print "Missing inputfile name!!"
        print "checksum.py -h <hash> -c <checksum> <inputfile>"
        sys.exit(2)

    #Lay thong tin input_file va output_file
    input_file = args[0]
    #---------------Xu ly xong tham so dong lenh-------------------

	#Goi ham checksum
    tmp = check_sum(hash,mychecksum,input_file)
    if( tmp == True or tmp == False):
        print "Check checksum result:",tmp
    else:
        print "Checksum created:", tmp
    return
#=================================================================

if __name__ == "__main__":
    main(sys.argv[1:])
