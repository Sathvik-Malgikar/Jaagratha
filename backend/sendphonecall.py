# Download the helper library from https://www.twilio.com/docs/python/install

from twilio.rest import Client

# import pywhatkit
# Set environment variables for your credentials
# Read more at http://twil.io/secure

acc_sid = "ACf752e1366efedfa9110501db63e57e2d"
# auth_token = os.environ["TWILIO_AUTH_TOKEN"]
client = Client(acc_sid, "710ad5d75a616636a15c419237e5236c")
# client2 = Client("MGdff59a8612dba38b26e32f05e160a12c", "5fb65278ea9da536ee5fab6be2766080")


def say(msg,num):
    print(f"<Response><Say>{msg}</Say></Response>")
    call = client.calls.create(
    twiml=f"<Response><Say>{msg}</Say></Response>",
    # url="http://demo.twilio.com/docs/voice.xml",
    to="+91" + num,
    from_="+15073535912"
    )

    print(call.sid)
    # pywhatkit.sendwhatmsg_to_group_instantly("AB123CDEFGHijklmn", "Hey All!")
    
    # message = client2.messages.create(
    #                           body='Hello there!',
    #                           from_='whatsapp:+15073535912',
    #                           to='whatsapp:+91'+num
    #                       )

    # print(message.sid)