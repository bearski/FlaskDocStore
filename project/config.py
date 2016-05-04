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
    MAIL_SERVER = os.environ['MAILGUN_SMTP_SERVER']
    MAIL_PORT = os.environ['MAILGUN_SMTP_PORT']
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ['MAILGUN_SMTP_LOGIN']
    MAIL_PASSWORD = os.environ['MAILGUN_SMTP_PASSWORD']
    MAIL_DEFAULT_SENDER = os.environ['MAILGUN_SMTP_LOGIN']

    # db connection
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
