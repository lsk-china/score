from pyBases import *
from pyLog import Logger

import smtplib
from email.mime.text import MIMEText
from email.header import Header

smtp = smtplib.SMTP()
log = Logger("Mail Sender")
connected = false

def connect(host,username,password):
	log.info("Connecting to SMTP server: "+host)
	try:
		smtp.connect(host,25)
		smtp.login(username,password)
		global connected
		connected = true
	except Exception as e:
		log.error("Connect failed: ",e)

def send(text,fromAddr,toAddr,subject,encoding="utf-8"):
	msg = MIMEText(text,"plain",encoding)
	msg["From"] = Header(fromAddr,encoding)
	msg["To"] = Header(toAddr,encoding)
	msg["Subject"] = Header(subject,encoding)
	if not connected:
		log.error("Cannot send email: Not connected")
		return
	try:
		smtp.sendmail(fromAddr,toAddr,msg.as_string())
	except Exception as e:
		log.error("Cannot send email: "`,e)
