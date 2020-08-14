##############################################
#######		By Arijit bhowmick	#####
##############################################

import os

print("#"*27, "\nRockstar_encoded decoding as ASCII\n", "#"*27, "\n\n")

ascii_enc = open("rockstar_code_enc.txt", "r")

ascii_enc_list = ascii_enc.readlines()

ascii_enc.close()

print("Flag --> picoCTF{", end="")

for ascii_ in ascii_enc_list:
	print(chr(int(ascii_.replace("\n", ""))), end="")
print("}")
