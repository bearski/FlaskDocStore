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
    # MAIL_USE_TLS = False
    # MAIL_USE_SSL = True

    MAIL_SERVER = os.environ['MAILGUN_SMTP_SERVER']
    MAIL_PORT = 587
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True


    # gmail authentication
    # MAIL_USERNAME = os.environ['APP_MAIL_USERNAME']
    # MAIL_PASSWORD = os.environ['APP_MAIL_PASSWORD']

    MAIL_USERNAME = os.environ['MAILGUN_SMTP_LOGIN']
    MAIL_PASSWORD = os.environ['MAILGUN_SMTP_PASSWORD']


    # mail accounts
    # MAIL_DEFAULT_SENDER = os.environ['APP_MAIL_DEFAULT_SENDER']
    MAIL_DEFAULT_SENDER = os.environ['MAILGUN_SMTP_LOGIN']

    #SQLALCHEMY_DATABASE_URI = os.environ['APP_SQLALCHEMY_DATABASE_URI']
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

#class DevelopmentConfig(BaseConfig):
#    """Development configuration."""
#    DEBUG = True
#    WTF_CSRF_ENABLED = False
#    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'dev.sqlite')
#    DEBUG_TB_ENABLED = True
#
#
class TestingConfig(BaseConfig):
    """Testing configuration."""
    TESTING = True
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 1
    WTF_CSRF_ENABLED = False
#    SQLALCHEMY_DATABASE_URI = 'sqlite://'


class ProductionConfig(BaseConfig):
    """Production configuration."""
    STRIPE_SECRET_KEY = 'foo'
    STRIPE_PUBLISHABLE_KEY = 'bar'
