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
    time.sleep(2)
    for curnum,curmail in zip(num,email):
        print(f"now mailing {curmail}")
        mail(f"{msg} {location}",email=curmail)

        print("done")
        smsfoo(msg=msg,num=curnum,loc=location)
        print("done")
        time.sleep(2)
    
# GRAND("Medium level security is raised in Dwarakanagar. Get Moving! ","https://goo.gl/maps/ZcTaE9kFN5GL1CU67",["7019486115","8762671367"],["sathvik.malgikar@gmail.com","amrithagk12@gmail.com"])
    