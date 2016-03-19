#!/usr/bin/python
#encrypt.py –m <mode> –i <IV> <input_file> <output_file>

import sys, getopt

def main(argv):

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
			mode = arg
		elif opt == "-i"
			IV = arg
			
	
