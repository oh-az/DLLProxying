import sys
import os
from colorama import Fore

def checkFile():
	global fileName
	global directory
	if len(sys.argv) != 3:
	    print(Fore.BLUE + "Usage: " + sys.argv[0] + " <DLL> <Original DLL Directory>\nExamples:\npython dllProxy.py dpapi.dll SysWOW64\npython dllProxy.py cscapi.dll System32\n\n")
	    quit()

	fileName = sys.argv[1]
	directory = sys.argv[2]
	if not os.path.exists(fileName):
	    print(Fore.RED +"ERROR! " + fileName + " DOES NOT EXIST..\n\n")
	    quit()
