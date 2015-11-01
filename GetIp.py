#!/usr/local/bin/python
import netifaces
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import datetime
import urllib2


def wait_for_internet_connection():
    while True:
        try:
            response = urllib2.urlopen('http://www.wunderground.com', timeout=1)
            return
        except urllib2.URLError:
            pass

print("Waiting for Internet Connection")
wait_for_internet_connection()

body = "Message Begin --\n"

print("Obtaining interface information")
interfaces = netifaces.interfaces()
for i in interfaces:
    if i == 'lo':
        continue
    iface = netifaces.ifaddresses(i).get(netifaces.AF_INET)
    if iface != None:
        for j in iface:
            body += j['addr'] + "\n"

body += "Message End --"


fromaddr = "FROM_EMAIL"
toaddr = "TO_EMAIL"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "BeagleBoneBlack - IP address " + str(datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p"))

msg.attach(MIMEText(body, 'plain'))

print("Connecting...")
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
print("Logging in")
server.login(fromaddr, "PASSWORD_HERE")
text = msg.as_string()
print("Message Sent")
server.sendmail(fromaddr, toaddr, text)
server.quit()
print("Close")
