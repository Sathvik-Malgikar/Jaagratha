# import smtplib
# from os.path import basename
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from email.mime.application import MIMEApplication
# import sys
# import time

# from_addr = 'Jaagratha_Autodetect@outlook.com'
# # to_addr = 'me@example.com'
# subject = 'Alert from HeadQuarters'
# # content = 'How neat is that?'


# server = smtplib.SMTP('smtp-mail.outlook.com',587)

# server.starttls()

# server.login(from_addr,'securityDetect')

# # seconds = sys.argv[3]
# # # arr = seconds.split(":")
# # # print(arr[0])
# # # print(arr[1])
# # # seconds=0
# # # seconds+=arr[1] *60+ arr[0] * 3600
# # print("waiting for ",seconds)
# # time.sleep( int( seconds))

# def mail(msgappend,email):
#     msg = MIMEMultipart()
#     msg['From'] = from_addr
#     msg['To'] = email
#     msg['Subject'] = subject
#     body = MIMEText(msgappend, 'plain')
#     msg.attach(body)
    
#     filename = 'suspect.jpg'
#     with open(filename, 'r') as f:
#         imgname = f.name
#         imgdata = f.name
#         imgtype = "jpeg"
        
#         # part = MIMEApplication(f.read(), Name=basename(filename))
#         # part['Content-Disposition'] = 'attachment; filename="{}"'.format(basename(filename))
        
#     msg.attach(part)
    
#     server.sendmail("Jaagratha_Autodetect@outlook.com",email,msg=msg)

#     print("mail sent to ",email,"content : ",msgappend)

    
import smtplib
import imghdr
from email.message import EmailMessage

# server = smtplib.SMTP('smtp-mail.outlook.com',587)

# server.starttls()

Sender_Email = "autodetectcrimesjaagratha@gmail.com"
newMessage = EmailMessage()                         
newMessage['Subject'] = "Alert from HeadQuarters" 
newMessage['From'] = Sender_Email                   
# server.login(Sender_Email,'securityDetect')


def mail(msgappend,email):

    # Reciever_Email = "codeitbro@gmail.com"
    Password = "yawyqwvxualxvnbe"

    newMessage['To'] = email                   
    newMessage.set_content(msgappend) 

    with open('suspect.png', 'rb') as f:
        image_data = f.read()
        image_type = imghdr.what(f.name)
        image_name = f.name

    newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465 ) as smtp:

        smtp.login(Sender_Email, Password)              
        smtp.send_message(newMessage)
        
    # server.sendmail("Jaagratha_Autodetect@outlook.com",email,msg=newMessage)

    print("mail sent to ",email,"content : ",msgappend)