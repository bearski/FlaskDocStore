# project/models.py

import datetime
from project import db, bcrypt
from hashlib import md5
from sqlalchemy import Enum

class Address(db.Model):
    __tablename__ = "address"
    id = db.Column(db.Integer, primary_key=True)
    pobox = db.Column(db.String(10))
    building = db.Column(db.String(140))
    streetname = db.Column(db.String(140))
    suburb = db.Column(db.String(140))
    city = db.Column(db.String(140))
    state = db.Column(db.String(140))
    postalcode = db.Column(db.String(10))
    country = db.Column(db.String(140))

    def __repr__(self):
        return '<id {}'.format(self.id)


class Telephone(db.Model):
    __tablename__ = "telephone"
    id = db.Column(db.Integer, primary_key=True)
    phonetype_id = db.Column(db.Integer)
    countrycode = db.Column(db.String(5))
    areacode = db.Column(db.String(5))
    telno = db.Column(db.Integer)

    def __repr__(self):
        return '<id {}'.format(self.id)


class User(db.Model):
    __tablename__ = "human"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    username = db.Column(db.String(60), unique=True, nullable=True)
    firstname = db.Column(db.String(60), nullable=True)
    surname = db.Column(db.String(60), nullable=True)
    about_me = db.Column(db.String(400), nullable=True)
    gender = db.Column(Enum("female", "male", name="gender_enum"), nullable=True)
    birthdate = db.Column(db.DateTime, nullable=True)
    password = db.Column(db.String, nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    confirmed = db.Column(db.Boolean, nullable=False, default=False)
    confirmed_on = db.Column(db.DateTime, nullable=True)
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'), nullable=True)
    telephone_id = db.Column(db.Integer, db.ForeignKey('telephone.id'), nullable=True)

    def __init__(self, email, password, admin=False, confirmed=False, confirmed_on=None):
        self.email = email
        self.password = bcrypt.generate_password_hash(password)
        self.admin = admin
        self.confirmed = confirmed
        self.confirmed_on = confirmed_on
        self.username = email

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def avatar(self, size):
        return 'http://www.gravatar.com/avatar/%s?d=mm&s=%d' % (md5(self.email.encode('utf-8')).hexdigest(), size)

    def __repr__(self):
        return '<email {}'.format(self.email)


class Employment(db.Model):
    __tablename__ = "employment"
    id = db.Column(db.Integer, primary_key=True)
    human_id = db.Column(db.Integer, db.ForeignKey('human.id'), nullable=False)
    employer = db.Column(db.String(200), nullable=False)
    position = db.Column(db.String(140), nullable=False)
    job_desc = db.Column(db.String(200), nullable=True)
    start_date = db.Column(db.DateTime, nullable=True)
    end_date = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return '<id {}'.format(self.id)


class EducationalInstitutionType(db.Model):
    __tablename__ = "educationalinstitutiontype"
    id = db.Column(db.Integer, primary_key=True)
    educational_institution_type = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<id {}'.format(self.id)


class Education(db.Model):
    __tablename__ = "education"
    id = db.Column(db.Integer, primary_key=True)
    human_id = db.Column(db.Integer, db.ForeignKey('human.id'), nullable=False)
    educational_institution = db.Column(db.String(200), nullable=False)
    educational_institution_type_id = db.Column(db.Integer, nullable=True)
    course_studied = db.Column(db.String(200), nullable=True)
    start_date = db.Column(db.DateTime, nullable=True)
    end_date = db.Column(db.DateTime, nullable=True)
    accolades = db.Column(db.String(400), nullable=True)

    def __repr__(self):
        return '<id {}'.format(self.id)


# publication
# presentations
# patents
# products
# research
