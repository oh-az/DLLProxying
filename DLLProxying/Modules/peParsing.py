import pefile
from Modules import check
from colorama import Fore




def parse():
	dirr = [pefile.DIRECTORY_ENTRY["IMAGE_DIRECTORY_ENTRY_EXPORT"]]
	pe = pefile.PE(check.fileName)
	pe.parse_data_directories(directories=dirr)
	allExports = [i.name for i in pe.DIRECTORY_ENTRY_EXPORT.symbols]
	for export in allExports:
		print(Fore.GREEN + '#pragma comment(linker, "/export:'+ str(export).replace("b","").replace("'","") + '=\\"C:\\\\Windows\\\\System32\\\\' + str(check.fileName.strip(".dll").split("/")[-1]) + "." + str(export).replace("b","").replace("'","") +'\\"")')
	print("\n")