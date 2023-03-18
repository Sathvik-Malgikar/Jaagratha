# Download the helper library from https://www.twilio.com/docs/python/install

from twilio.rest import Client
import keys

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure

client = Client(keys.account_sid, keys.auth_token)


def smsfoo(msg,num):
    message = client.messages.create(
                                from_=keys.twilio_num,
                                body=msg,
                                to="+91"+num
                            )
    print(message.sid)  
