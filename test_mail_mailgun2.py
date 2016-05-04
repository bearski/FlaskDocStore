import os
from flask.ext.mail import Mail, Message
from flask import Flask, render_template, url_for, redirect, send_from_directory
from flask import request

from project.email import send_email

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])

mail = Mail(app)

subject = "test email"
html = "test email" 

send_email('santosh.sewlal@gmail.com', subject, html)
