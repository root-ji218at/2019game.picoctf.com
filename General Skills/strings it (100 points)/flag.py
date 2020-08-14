##############################################
#######		By Arijit bhowmick	#####
##############################################

import os

print("#"*27, "\nFound flag using grep command (commandline -> linux)\n", "#"*27, "\n\n")

os.system('strings strings | grep "picoCTF"')
