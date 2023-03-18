from sendphonecall import say
from sendemail import mail
from sms import smsfoo
# import pywhatkit
# pywhatkit.start_server()

# pywhatkit.sendwhatmsg("+916360709909", "Hello pywhat",8+12,2)

def GRAND(msg,location,num,email):
    say(f"{msg} ", num)
    mail(f"{msg} {location}",email=email)
    smsfoo(msg=msg,num=num)
    
# GRAND("Medium level security is raised in Dwarakanagar. Get Moving! ","https://goo.gl/maps/ZcTaE9kFN5GL1CU67","7483064938","hemabhushanr3@gmail.com")
    