
class Contact:
	def __init__(self, name, email):
		self.name = name
		self.email = email

	def __str__(self):
		return "%s: %s" % (self.name, self.email)
