from Modules import intro, check, peParsing
from colorama import Fore



def main():
    intro.introMsg()
    check.checkFile()
    print(Fore.BLUE + "\t DLL : " + Fore.RED + str(check.fileName.split("/")[-1]))
    print(Fore.BLUE + "\t\t\t\t\tPaste this at the top of your DLL code\n")
    peParsing.parse()

main()