from twilio.rest import Client

TWILIO_SID = "AC77b10621626f2d1545a98258162f8235"
TWILIO_AUTH_TOKEN = "db543a176c698ce690b05d8eda8e31e4"
TWILIO_VIRTUAL_NUMBER = "+15164004128"
TWILIO_VERIFIED_NUMBER = "+9779806736272"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
