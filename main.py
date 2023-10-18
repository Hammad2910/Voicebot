from twilio.rest import Client
import keys

client=Client(keys.account_sid,keys.auth_token)

call=client.calls.create(
    url='http://demo.twilio.com/docs/voice.xml',
    to=keys.my_number,
    from_=keys.twilio_number
)


print(call.sid)
# message = client.messages.create(
  
#   from_='+15176495424',
#   body='Hello',
#   to='+923330492952'
# )
