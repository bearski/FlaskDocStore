# project/models.py

import datetime
from project import db, bcrypt
from hashlib import md5
# from sqlalchemy import Enum


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


class Gender(db.Model):
    __tablename__ = "gender"
    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return self.gender


class User(db.Model):
    __tablename__ = "human"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    username = db.Column(db.String(60), unique=True, nullable=True)
    firstname = db.Column(db.String(60), nullable=True)
    surname = db.Column(db.String(60), nullable=True)
    about_me = db.Column(db.String(400), nullable=True)
    birthdate = db.Column(db.DateTime, nullable=True)
    password = db.Column(db.String, nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False,
                              default=datetime.datetime.utcnow)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    confirmed = db.Column(db.Boolean, nullable=False, default=False)
    confirmed_on = db.Column(db.DateTime, nullable=True)
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'),
                           nullable=True)
    telephone_id = db.Column(db.Integer, db.ForeignKey('telephone.id'),
                             nullable=True)
    gender_id = db.Column(db.Integer, db.ForeignKey('gender.id'))
    gender = db.relationship('Gender', backref=db.backref('human',
                                                          lazy='dynamic'))

    def __init__(self, email, password, admin=False, confirmed=False,
                 confirmed_on=None):
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
        return 'http://www.gravatar.com/avatar/%s?d=mm&s=%d' % (md5(
            self.email.encode('utf-8')).hexdigest(), size)

    def __repr__(self):
        return '<email: {}'.format(self.email)


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
    __tablename__ = "educational_institution_type"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return self.description


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
    educational_institution_type_id = db.Column(db.Integer,
                                                db.ForeignKey('educational_institution_type.id'))
    educational_institution_type = db.relationship('EducationalInstitutionType',
                                                   backref=db.backref('education',
                                                                      lazy='dynamic'))

    def __repr__(self):
        return '<id: {}'.format(self.id)


class PublicationCategory(db.Model):
    __tablename__ = "publication_category"
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return self.category


class Publication(db.Model):
    __tablename__ = "publication"
    id = db.Column(db.Integer, primary_key=True)
    human_id = db.Column(db.Integer, db.ForeignKey('human.id'), nullable=False)
    title = db.Column(db.String(10), nullable=False)
    authors = db.Column(db.String(250), nullable=True)
    publication_date = db.Column(db.DateTime, nullable=True)
    publisher = db.Column(db.String(250), nullable=True)
    publication_url = db.Column(db.String(100), nullable=True)
    description = db.Column(db.String(250), nullable=True)
    publication_category_id = db.Column(db.Integer,
                                        db.ForeignKey('publication_category.id'))
    publication_category = db.relationship('PublicationCategory',
                                           backref=db.backref('publication',
                                                              lazy='dynamic'))

    def __repr__(self):
        return self.id


class PatentOffice(db.Model):
    __tablename__ = "patent_office"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return self.name


class PatentStatus(db.Model):
    __tablename__ = "patent_status"
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(20), nullable=False)

    def __repr__(self):
            return self.status


class Patent(db.Model):
    __tablename__ = "patent"
    id = db.Column(db.Integer, primary_key=True)
    human_id = db.Column(db.Integer, db.ForeignKey('human.id'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    patent_number = db.Column(db.String(20), nullable=False)
    inventors = db.Column(db.String(250), nullable=False)
    issue_date = db.Column(db.DateTime, nullable=True)
    patent_office_id = db.Column(db.Integer, db.ForeignKey('patent_office.id'))
    patent_office = db.relationship('PatentOffice', backref=db.backref('patent', lazy='dynamic'))
    patent_status_id = db.Column(db.Integer, db.ForeignKey('patent_status.id'))
    patent_status = db.relationship('PatentStatus', backref=db.backref('patent', lazy='dynamic'))
    patent_url = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return self.status


### IMPROVE THIS - look at list of certification providers
class Certification(db.Model):
    __tablename__ = "certification"
    id = db.Column(db.Integer, primary_key=True)
    human_id = db.Column(db.Integer, db.ForeignKey('human.id'), nullable=False)
    name = db.Column(db.String(250), nullable=True)
    certification_number = db.Column(db.String(250), nullable=True)
    issue_date = db.Column(db.DateTime, nullable=True)
    expiry_date = db.Column(db.DateTime, nullable=True)
    certification_url = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return self.id


# presentations
# research