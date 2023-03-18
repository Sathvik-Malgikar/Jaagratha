import smtplib
import sys
import time

server = smtplib.SMTP('smtp-mail.outlook.com',587)

server.starttls()

server.login('Jaagratha_Autodetect@outlook.com','securityDetect')

# seconds = sys.argv[3]
# # arr = seconds.split(":")
# # print(arr[0])
# # print(arr[1])
# # seconds=0
# # seconds+=arr[1] *60+ arr[0] * 3600
# print("waiting for ",seconds)
# time.sleep( int( seconds))

def mail(msgappend,email):
    server.sendmail("Jaagratha_Autodetect@outlook.com",email,msg="\r\n\r\n"+msgappend+'<img src="data:image/jpg;base64,{{base64-data-string here}} />"'
)

    print("mail sent to ",email,"content : ",msgappend)

    