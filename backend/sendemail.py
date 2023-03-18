import smtplib
import sys
import time

server = smtplib.SMTP('smtp-mail.outlook.com',587)

server.starttls()

server.login('imilysadul@outlook.com','Schedemail')

seconds = sys.argv[3]
# arr = seconds.split(":")
# print(arr[0])
# print(arr[1])
# seconds=0
# seconds+=arr[1] *60+ arr[0] * 3600
print("waiting for ",seconds)
time.sleep( int( seconds))

server.sendmail("imilysadul@outlook.com",sys.argv[1],msg="\r\n\r\n"+sys.argv[2])

print("mail sent to ",sys.argv[1],"content : ",sys.argv[2])