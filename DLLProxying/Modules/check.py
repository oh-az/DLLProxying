import sys
import os
from colorama import Fore

def checkFile():
	global fileName
	if len(sys.argv) != 2:
	    print(Fore.BLUE + "Usage: " + sys.argv[0] + " <DLL>\n\n")
	    quit()

	fileName = sys.argv[1]
	if not os.path.exists(fileName):
	    print(Fore.RED +"ERROR! " + fileName + " DOES NOT EXIST..\n\n")
	    quit()