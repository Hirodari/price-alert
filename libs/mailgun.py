from requests import post
import os

# load_dotenv()

class Mailgun:
	def __init__(self, message):
		# self.receipient = receipient
		# self.subject = subject
		self.message = message
		self.domain = os.environ.get("MAILGUN_DOMAIN")
		self.api = os.environ.get("MAILGUN_API")

	def send_simple_message(self):
		response = post(
			f"{self.domain}",
			auth=("api", f"{self.api}"),
			data={"from": "Excited User <fredbitenyo@afrikoacafe.com>",
				"to": ["hirodaridev@gmail.com"],
				"subject": "Alerts for Pricing",
				"text": self.message})
		if response.status_code != 200:
			print(response.json())

		return response


# mailgun = Mailgun("My first mail", "My first mailgun class to send an email")
# print(Mailgun("My final mailgun class to test").send_simple_message())