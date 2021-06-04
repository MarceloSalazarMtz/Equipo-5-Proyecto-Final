import os
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException


def notify_police(type, percentage):
    service = TwilioService()
    try:
        service.send_message("Detected a " + type +
                             " with " + percentage + "% accurary, Sending police unit to Parque Rufino Tamayo. ETA: 10 minutes")
        return {'message': 'message was sent'}
    except TwilioRestException as e:
        print(e)


class TwilioService:
    client = None

    def __init__(self):
        account_sid = os.environ.get('TWILIO_SID')
        auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
        self.client = Client(account_sid, auth_token)

    def send_message(self, message):
        agent_phone_number = os.environ.get('POLICE_NUMBER')
        twilio_phone_number = os.environ.get('TWILIO_NUMBER')
        self.client.messages.create(to=agent_phone_number,
                                    from_=twilio_phone_number,
                                    body=message)
