from sendphonecall import say
from sendemail import mail
from sms import smsfoo
# import pywhatkit
# pywhatkit.start_server()

# pywhatkit.sendwhatmsg("+916360709909", "Hello pywhat",8+12,2)

def GRAND(msg,location):
    say(f"{msg} ", "7483064938")
    mail(f"{msg} {location}","hemabhushanr3@gmail.com")
    smsfoo(msg=msg,num="7483064938")
    
GRAND("Medium level security is raised in Dwarakanagar. Get Moving! ","https://goo.gl/maps/ZcTaE9kFN5GL1CU67")
    