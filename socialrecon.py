from url import urlinfo
from iplocator import iplocate
from webscrap import Links
from number import number
import time
import sys
from url import urlinfo
from pdfanalysis import pdfinfo
from imagerecon import recon
from iplocator import iplocate
from TraceIP import read_multiple_ip
from webscrap import Links
from NameInfo import Nameinfo
from number import number
R = '\033[1;31;40m' 
G = '\033[1;32;40m'
C = '\033[1;36;40m'
Y = '\033[1;33;40m' 
def reconinput():
    inp=input("Info>> ")
    if (inp=='1'):
        iplocate()
    elif(inp =='2'):
        urlinfo()
    elif(inp=='3'):
        Links()
    elif (inp=='4'):
        number()
    elif(inp=='exit'):
        exit()
    elif(inp=='tools'):
        print(G+"""Tools available 
    
            1.Trace Single IP
            2.URL redirection checker
            3.Open Links
            4.Phonenumber verifier
            
            
            usage : type exit to stop
            """)
    else:
        print(R+"Enter an valid option")
    while True:
        reconinput()
        
if __name__=="__main__":
   reconinput()
     
    
