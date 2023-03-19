# # Download the helper library from https://www.twilio.com/docs/python/install

# from twilio.rest import Client
# import keys

# # Find your Account SID and Auth Token at twilio.com/console
# # and set the environment variables. See http://twil.io/secure

# client = Client(keys.account_sid, keys.auth_token)


# def smsfoo(msg,num,loc):
#     message = client.messages.create(
#                                 from_=keys.twilio_num,
#                                 body=msg + f"Move to this location : {loc}",
#                                 to="+91"+num
#                             )
#     print(message.sid)  

# Install Courier SDK: pip install trycourier
# from trycourier import Courier

# client = Courier(auth_token="pk_prod_6836594WHPM740JR3XPQG2W8RXPQ")

# resp = client.send_message(
# message={
#     "to": {
#     "email": "Sathvik.malgikar@gmail.com"
#     },
#     "content": {
#     "title": "Welcome to Courier!",
#     "body": "Want to hear a joke? {{joke}}"
#     },
#     "data":{
#     "joke": "Why does Python live on land? Because it is above C level"
#     }
# }
# )

from twilio.rest import Client

account_sid = 'ACf752e1366efedfa9110501db63e57e2d'
auth_token = '710ad5d75a616636a15c419237e5236c'
client = Client(account_sid, auth_token)


def smsfoo(msg,num,loc):
    message = client.messages.create(
    from_='whatsapp:+14155238886',
    body=f'**Alert from headquarters**{msg} Location: {loc}',
    to='whatsapp:+91'+num
    )

    print(message.sid)