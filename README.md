# DLLProxying
DLL Proxying Tool To Generate The Export Directives For The Linker (C/C++)

![Capture](https://user-images.githubusercontent.com/74332587/204101004-36a41f23-5df3-4cfb-855f-19121a9c572c.PNG)



# Installation

1. Download the repo to your machine.
2. Move to the directory
```
cd DLLProxying
```
3. Install Requierments:
```
sudo pip3 install -r requierments.txt
```

# Usage
dllProxy.py (DLL) (Original DLL Directory)  
                                                                                                         
Examples:                                                                                                                                                   
```
python dllProxy.py dpapi.dll SysWOW64     
python dllProxy.py cscapi.dll System32 
```
2. Copy the output and paste it to your DLL code.


