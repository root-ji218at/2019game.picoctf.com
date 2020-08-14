##############################################
#######		By Arijit bhowmick	#####
##############################################

import base64

print("#"*27, "\nbase64 Decoder\n", "#"*27, "\n\n")

encoded_flag = open("encoded_flag.txt", 'r')

enc_flag_rd = (encoded_flag.readline()).replace("\n", "")

encoded_flag.close()

print("Flag --> picoCTF{"+(base64.b64decode(enc_flag_rd)).decode()+"}")
