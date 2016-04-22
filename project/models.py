# project/models.py


import datetime

from project import db, bcrypt


class User(db.Model):
    __tablename__ = "user_login"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    confirmed = db.Column(db.Boolean, nullable=False, default=False)
    confirmed_on = db.Column(db.DateTime, nullable=True)

    def __init__(self, email, password, admin=False, confirmed=False, confirmed_on=None):
        self.email = email
        self.password = bcrypt.generate_password_hash(password)
        self.admin = admin
        self.confirmed = confirmed
        self.confirmed_on = confirmed_on

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def __repr__(self):
        return '<email {}'.format(self.email)


class UserData(db.Model):
    __tablename__ = "user_info"

    id = db.Column(db.Integer, primary_key=True)
    user_login_id = db.Column(db.Integer, db.ForeignKey('user_login.id'), nullable=False)
    surname = db.Column(db.String, unique=True, nullable=True)
    firstname = db.Column(db.String, nullable=True)
    initials = db.Column(db.String, nullable=True)
    maiden_name = db.Column(db.String, nullable=True)
    idtype = db.Column(db.String, nullable=False)
    idnumber = db.Column(db.String, nullable=False)
    race = db.Column(db.String, nullable=True)
    gender = db.Column(db.String, nullable=True)
    birthdate  = db.Column(db.DateTime, nullable=True)
    alt_email = db.Column(db.String, nullable=True)
    telno = db.Column(db.String, nullable=True)
    notification = db.Column(db.Boolean, nullable=False, default=False)
    fulltimestudent = db.Column(db.Boolean, nullable=False, default=False)
    current_org = db.Column(db.String, nullable=True)

    def __init__(self, userid, idtype, idnumber):
        self.userid = userid
        self.idtype = idtype
        self.idnumber = idnumber

    def __repr__(self):
        return '<idnumber {}'.format(self.idnumber)
