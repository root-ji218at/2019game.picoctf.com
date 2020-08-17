import os

a = 1000

while a!=0:
	try:
		b = "tar -xvf "+str(a)+".tar"
		os.system(b)
		a -= 1
		print("extracted"+a+".tar")
	except:
		continue
		a -= 1
