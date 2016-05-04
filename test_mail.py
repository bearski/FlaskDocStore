import os
from flask.ext.mail import Mail, Message
from flask import Flask, render_template, url_for, redirect, send_from_directory
from flask import request

app = Flask(__name__)

app.config.update(
    dict(
        MAIL_SERVER = 'smtp.gmail.com',
        MAIL_PORT =  587,
        MAIL_USE_TLS = True,
        MAIL_USERNAME = 'santosh.sewlal@gmail.com',
        MAIL_PASSWORD = 's4nt0shisb3ar'
    )
)

ADMINS = ['santosh.sewlal@gmail.com']

msg = Message('test subject', sender=ADMINS[0], recipients=ADMINS)
msg.body = 'text body'
msg.html = '<b>HTML</b> body'

mail = Mail(app)

with app.app_context():
    mail.send(msg)

