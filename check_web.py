#!/usr/bin/env python3
# checks whether a URL responds with an https status of 200 and send an email if it does not. 
# Usage: check_web.py [url]


import urllib.request, urllib.error
import smtplib
import email.message
import sys

def send_message(msg, url):
    sender = 'system@zillow.com'
    recipient = 'response_team@zillow.com'
    passwd = 'Insert_Password_Here'
    server = smtplib.SMTP_SSL('mail.zillow.com', 465)
    server.login(sender, passwd)
    sub = (url + " is responding with " + msg)
    et = email.message.Message()
    et['From'] = sender 
    et['To'] = recipient
    et['Subject'] = sub
    try:
        server.sendmail(sender, recipient, et.as_string())
        print ('sending mail')
    except:
        print ('error sending mail')
    server.quit()

def main():
    url = sys.argv[1]
    try:
        conn = urllib.request.urlopen(url)
    except urllib.error.HTTPError as exception:
        msg = ('HTTPError: {}'.format(exception.code))
        send_message(msg, url)
    except urllib.error.URLError as exception:
        msg = ('URLError: {}'.format(exception.reason))
        send_message(msg, url)
    else:
        print('All is well')

main()
