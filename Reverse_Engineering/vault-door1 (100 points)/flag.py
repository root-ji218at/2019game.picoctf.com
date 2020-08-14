enc = open("enc.txt", "r")
enc_read = enc.readlines()
enc.close()

replaced_enc_lst = []

for line in enc_read:
	replaced_enc_lst += [(((((line.replace("' &&", "")).replace("\n", "")).replace("               password.charAt(", "")).replace(")", "")).replace(" ", "")).replace("'", "")]

place = []
flag_chr = []

for shorting_element in replaced_enc_lst:
	element = shorting_element.split("==")
	place += [element[0]]
	flag_chr += [element[1]]

count = 0

print("Flag --> picoCTF{", end="")

while count!=len(place):
	place_index =  place.index(str(count))
	print(flag_chr[place_index], end="")
	count +=1
print("}")
