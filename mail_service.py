import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class MailService:
	def __init__(self, host, port, user, password):
		self.host = host
		self.port = port
		self.user = user
		self.password = password
		self.connection = None
		self._subject = ""

	def subject():
	    doc = "The subject property."
	    def fget(self):
	        return self._subject
	    def fset(self, value):
	        self._subject = value
	    def fdel(self):
	        del self._subject
	    return locals()
	
	subject = property(**subject())

	@property
	def from_email(self):
		return self._from_email

	@from_email.setter
	def from_email(self, from_email):
		self._from_email = from_email

	@from_email.deleter
	def from_email(self):
		del self._from_email

	def get_connection(self):
		if self.connection is None:
			# Open a connection to the SendGrid mail server
			s = smtplib.SMTP(self.host, self.port)
			# Authenticate
			s.login(self.user, self.password)
			self.connection = s

		return self.connection

	def close(self):
		"""
		Close smtp connection.
		"""
		if not self.connection is None:
			self.connection.close()
		 
	def send_email(self, to_email, plain_text, html_text, **kwargs):
		"""
		Send an email to a specific email address
		- to_email: valid destination email
		- plain_text: plain text to send, may be used by mail clients that cannot
		   read HTML text
		- html_text: html text to send, may be used by mail clients that cam
		   read HTML text
		- subject: email subject. If not included, default subject will be used
		- from_email: email to send the email on behalf of. If not included,
		   default from_email will be used
		"""

		if 'subject' in kwargs:
			subject = kwargs['subject']
		else:
			subject = self.subject

		if 'from_email' in kwargs:
			from_email = kwargs['from_email']
		else:
			from_email = self.from_email

		msg = MIMEMultipart('alternative')
		msg['Subject'] = subject
		msg['From'] = from_email
		msg['To'] = to_email

		plain_part = MIMEText(plain_text, 'plain')
		html_part = MIMEText(html_text, 'html')
		# Attach parts into message container.
		msg.attach(plain_part)
		msg.attach(html_part)

		self.get_connection().sendmail(from_email, to_email, msg.as_string())

