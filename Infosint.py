from socialrecon import reconinput
from socmint import banner
from socmint import search

cyan="\033[1;36;40m"
green="\033[1;32;40m"
red="\033[1;31;40m"
Y = '\033[1;33;40m'

def Main(a):
    if(a==1):
        reconinput()
    elif(a==2):
        banner()
        search()
if __name__=="__main__":
    print(cyan+"""

|$$$$$$\$$$$$$$\ $$$$$$\                   $$\          $$\     
|$$ __/ \____$$ |$$___/                    \__|         $$ |    
|$$|_        $$/ $$ \__    $$$$$$\  $$$$$$$\$$\$$$$$$$\$$$$$$\   
|$$$$$$\/$$$$$$| $$$$$$\  $$  __$$\$$  _____$$ $$  __$$\_$$  _|  
|$$/ $$ \___ $$\     $$ | $$ /  $$ \$$$$$$\ $$ $$ |  $$ |$$ |    
|$$\_$$|     $$ |    $$  \$$ |  $$ |\____$$\$$ $$ |  $$ |$$ |$$\ 
|$$$$$$\$$$$$$$/ $$$$$$/  \$$$$$$  $$$$$$$  $$ $$ |  $$ |\$$$$  |
\______/\_____/\_________/\______/\_______/\__\__|  \__| \____/ 
    """)
    print(Y+"                           Created By : Chetti Thanmay Ram")
    print(Y+"                           Created By : Jala Ajay Kumar ")
    print(Y + "                         Created By : Raviteja Karumanchi ")
    print(green+"""
                Available Modules 
           
           1.OSNIT,
           2.SOCMINT
    """) 
    print(Y+"Note : In OSNIT type 'tools' to find tools.")
    print(Y+"Note : In SOCMINT type user name.")
    a=int(input("Module >> "))
    Main(a)
    