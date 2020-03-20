# Author : ELaoShi
# Version: 1.0.0

from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC2xxxxxxxxxxxxxxxxxxxxxxxxxxxxx92"
# Your Auth Token from twilio.com/console
auth_token  = "dc6xxxxxxxxxxxxxxxxxxxxxxx5b35"


client = Client(account_sid, auth_token)

sms_to = "+xx12345678"

template_body_v1 = "Hello Mr Eric, welcome to the Eric Portal. it's great to have you onboard!"

twilio_phone_number = "ELaoShi"
message = client.messages.create(
    to=sms_to,
    from_=twilio_phone_number,
    body=template_body_v1)

print(message.sid)

# Done
