# project/config.py

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(object):
    """Base configuration."""
    SECRET_KEY = 'bestSecretKeyEver'
    SECURITY_PASSWORD_SALT = 'bestSecurityPasswordSaltEver'
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 13
    WTF_CSRF_ENABLED = True
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    # mail settings
    # MAIL_SERVER = 'smtp.gmail.com'
    # MAIL_PORT = 465


    MAIL_SERVER = 'smtp.mailgun.org' # os.environ['MAILGUN_SMTP_SERVER']
    MAIL_PORT = 587 # os.environ['MAILGUN_SMTP_PORT']
    MAIL_USE_TLS = True


    # gmail authentication
    # MAIL_USERNAME = os.environ['APP_MAIL_USERNAME']
    # MAIL_PASSWORD = os.environ['APP_MAIL_PASSWORD']

    MAIL_USERNAME = 'postmaster@appbffbce930f264e479c9e27fd294518d6.mailgun.org' # os.environ['MAILGUN_SMTP_LOGIN']
    MAIL_PASSWORD = '1706b4fab5522717b7f68014bb7b39d9' # os.environ['MAILGUN_SMTP_PASSWORD']

    # MAILGUN_API_KEY = os.environ['MAILGUN_API_KEY']
    # MAILGUN_DOMAIN = os.environ['MAILGUN_DOMAIN']
    # MAILGUN_PUBLIC_KEY = os.environ['MAILGUN_PUBLIC_KEY']

    # mail accounts
    # MAIL_DEFAULT_SENDER = os.environ['APP_MAIL_DEFAULT_SENDER']
    MAIL_DEFAULT_SENDER =  'postmaster@appbffbce930f264e479c9e27fd294518d6.mailgun.org' # os.environ['MAILGUN_SMTP_LOGIN']

    #SQLALCHEMY_DATABASE_URI = os.environ['APP_SQLALCHEMY_DATABASE_URI']
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

class TestingConfig(BaseConfig):
    """Testing configuration."""
    TESTING = True
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 1
    WTF_CSRF_ENABLED = False

class ProductionConfig(BaseConfig):
    """Production configuration."""
    STRIPE_SECRET_KEY = 'foo'
    STRIPE_PUBLISHABLE_KEY = 'bar'
