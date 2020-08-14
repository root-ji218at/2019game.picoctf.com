##############################################
#######		By Arijit bhowmick	#####
##############################################


print("#"*27, "\nHexadecimal to Character Converter\n", "#"*27, "\n\n")
try:
	hex_value = str(input("Please Enter a \"Hex value\" to convert it to \"Character\" \n\n -->"))
	hex_value_ = hex_value.replace("0x", "")
	chr_ = chr(int(hex_value_, 16))
	print(chr_)
except:
	print("An error Occured")
