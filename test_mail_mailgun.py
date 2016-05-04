import os
from flask.ext.mail import Mail, Message
from flask import Flask, render_template, url_for, redirect, send_from_directory
from flask import request

app = Flask(__name__)

app.config.update(
    dict(
        MAIL_SERVER = 'smtp.mailgun.org',
        MAIL_PORT =  587,
        MAIL_USE_TLS = True,
        MAIL_USERNAME = 'postmaster@appbffbce930f264e479c9e27fd294518d6.mailgun.org',
        MAIL_PASSWORD = '1706b4fab5522717b7f68014bb7b39d9'        
    )
)

ADMINS = ['postmaster@appbffbce930f264e479c9e27fd294518d6.mailgun.org']
RECIPIENTS=['santosh.sewlal@gmail.com']

msg = Message('test subject', sender=ADMINS[0], recipients=RECIPIENTS)
msg.body = 'text body'
msg.html = '<b>HTML</b> body'

mail = Mail(app)

with app.app_context():
    mail.send(msg)

