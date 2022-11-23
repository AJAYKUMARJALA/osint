import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers.phonenumberutil import region_code_for_country_code
from phonenumbers.phonenumberutil import region_code_for_number
import pycountry

cyan="\033[1;36;40m"
green="\033[1;32;40m"
red="\033[1;31;40m"
Y = '\033[1;33;40m'
def number():
    phonenum = input("Enter Mobile Number with country code >> ")
    pn = phonenumbers.parse(phonenum)
    country = pycountry.countries.get(alpha_2=region_code_for_number(pn))
    print('')
    print(cyan+"Country : "+str(country.name))
    print(cyan+"Location : "+(geocoder.description_for_number(pn,"en")))
    print(cyan+"Carrier : "+carrier.name_for_number(pn,"en"))
    
if __name__=="__main__":
    number()
