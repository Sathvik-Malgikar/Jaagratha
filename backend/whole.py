from sendphonecall import say
from sendemail import mail
from sms import smsfoo
import time
# import pywhatkit
# pywhatkit.start_server()

# pywhatkit.sendwhatmsg("+916360709909", "Hello pywhat",8+12,2)

def GRAND(msg,location,num,email):
    
    print(f"now calling {num[0]}")
    primarynum= num[0]
    print("done")
   
    
    say(f"{msg} ", primarynum)
    for curnum,curmail in zip(num,email):
        print(f"now mailing {curmail}")
        mail(f"{msg} {location}",email=curmail)

        print("done")
        smsfoo(msg=msg,num=curnum,loc=location)
        print("done")
        time.sleep(1)
    
# GRAND("Medium level security is raised in Dwarakanagar. Get Moving! ","https://goo.gl/maps/ZcTaE9kFN5GL1CU67","7483064938","hemabhushanr3@gmail.com")
    