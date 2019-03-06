#!/usr/bin/python

import sys
import time
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

def logline(str):
	return "%s SEND2ME %s" %(time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime()), str)

print(logline(("Starting with sys.argv = [%s]" % (str(sys.argv)))))
fullpath = sys.argv[1]
filename = fullpath[fullpath.rfind("/")+1:]
print(logline("Sending file: fullpath : %s; filename: %s" % (fullpath, filename)))
fromaddr = "frank.pater@gmail.com"
toaddr = "fpater2@comcast.net"
 
msg = MIMEMultipart()
 
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Image from Motion"
 
body = "Here is an image captured by Motion"
 
msg.attach(MIMEText(body, 'plain'))
 
attachment = open(fullpath, "rb")
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "sym?siQa2HY")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()

print(logline("Done"))
