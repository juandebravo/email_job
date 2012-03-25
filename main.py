#! /usr/bin/python
 
# -*- coding: utf-8 -*-

import ConfigParser
import csv

from email_job.contact import Contact
from email_job.mail_service import MailService

config = ConfigParser.SafeConfigParser()
config.read('config.cfg')

# Load configuration
server_config = dict((k, v) for k, v in config.items("server"))
mail_config = dict((k, v) for k, v in config.items("email"))

# Load CSV file
contacts = csv.reader(open(mail_config['contacts'], 'rb'), delimiter=',')

# Create Contacts
contacts = [Contact(c[0], c[1]) for c in contacts if not c[0].startswith("#")]

s = server_config

# Create mail service
mail = MailService(s['host'], s['port'], s['username'], s['password'])
mail.subject = mail_config['subject']
mail.from_email = mail_config['from_email']

# Load mail template
text = mail_config['text']
html = mail_config['html'] % text

# Send an email to every contact
for index, contact in enumerate(contacts):
	print "\nSending email number %d to:" % (index+1)
	print "\t%s => %s" % (contact.name, contact.email)
	mail.send_email(contact.email, text, html)
 
mail.close()
