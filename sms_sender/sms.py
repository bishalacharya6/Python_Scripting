# Download the helper library from https://www.twilio.com/docs/python/install

from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.o/secure
account_sid = 'ACc86d6935bae6fbe245bb5c4c496074ca'
auth_token = 'ea3591ac19bc25d16d6d5ffa0b194730'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         from_='+15076154705',
         body='This message was sent from my Twilio phone number!',
         to='+9779826739212'
     )

print(message.body)