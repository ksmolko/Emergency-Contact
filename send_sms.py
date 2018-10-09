from twilio.rest import Client

def sendSMS(toNum, fromNum):
	account_sid = "ENTER_SID_HERE"
	auth_token = "ENTER_TOKEN_HERE"

	client = Client(account_sid, auth_token)

	message = client.messages.create(
		to=toNum,
		from_=fromNum,
		body="Your loved one is in distress")
