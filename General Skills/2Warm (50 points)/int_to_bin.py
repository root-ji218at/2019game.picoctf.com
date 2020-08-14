##############################################
#######		By Arijit bhowmick	#####
##############################################


print("#"*27, "\nInteger to binary Converter\n", "#"*27, "\n\n")
try:
	try:
		integer = int(input("Please Enter an integer(base 10) to convert it to binary(base 2) \n\n -->"))
	except:
		print("Please Enter an \"Integer(base 10)\" value")
		exit()
	binary_value = (str(bin(integer)).replace("0b", ""))
	print(binary_value)
except:
	print("An error Occured")
