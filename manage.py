# manage.py

import datetime
import os
import unittest
import coverage

from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

from project import app, db
from project.models import (
    User,
    EducationalInstitutionType,
    Gender,
    PatentOffice,
    PatentStatus,
    PublicationCategory
)

app.config.from_object(os.environ['APP_SETTINGS'])

migrate = Migrate(app, db)
manager = Manager(app)

# migrations
manager.add_command('db', MigrateCommand)


@manager.command
def test():
    """Runs the unit tests without coverage."""
    tests = unittest.TestLoader().discover('tests')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    else:
        return 1


@manager.command
def cov():
    """Runs the unit tests with coverage."""
    cov = coverage.coverage(branch=True, include='project/*')
    cov.start()
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
    cov.stop()
    cov.save()
    print('Coverage Summary:')
    cov.report()
    basedir = os.path.abspath(os.path.dirname(__file__))
    covdir = os.path.join(basedir, 'tmp/coverage')
    cov.html_report(directory=covdir)
    print('HTML version: file://%s/index.html' % covdir)
    cov.erase()


@manager.command
def create_db():
    """Creates the db tables."""
    db.create_all()


@manager.command
def drop_db():
    """Drops the db tables."""
    db.drop_all()

@manager.command
def create_admin():
    """Creates the admin user."""
    db.session.add(
        User(
            email="ad@min.com",
            password="admin",
            admin=True,
            confirmed=True,
            confirmed_on=datetime.datetime.now()
        )
    )
    db.session.commit()


@manager.command
def insert_lookup_data():
    # EducationalInstitutionType
    db.session.add(EducationalInstitutionType(description='High School'))
    db.session.add(EducationalInstitutionType(description='University'))
    db.session.add(EducationalInstitutionType(
        description='Technikons / Universities of Technology'))
    db.session.commit()

    # Gender
    db.session.add(Gender(gender='Female'))
    db.session.add(Gender(gender='Male'))
    db.session.commit()


    # PublicationCategory
    db.session.add(PublicationCategory(category='Peer-reviewed publications',
                                       description='reports of original '
                                                   'investigations; clinical '
                                                   'reports; letters to the '
                                                   'editor'))

    db.session.add(PublicationCategory(category='Books - authoured',
                                       description='books authoured/written'))

    db.session.add(PublicationCategory(category='Books - edited',
                                       description='books edited'))

    db.session.add(PublicationCategory(category='Monographs - authoured',
                                       description='Monographs authoured'))

    db.session.add(PublicationCategory(category='Monographs - edited',
                                       description='Monographs edited'))

    db.session.add(PublicationCategory(category='Works in progress',
                                       description='Complete articles published '
                                                   'in conference proceedings, '
                                                   'chapters in books; review '
                                                   'articles; editorials.'))

    db.session.add(PublicationCategory(category='Development of educational materials',
                                       description='e.g. teaching cases'))

    db.session.add(PublicationCategory(category='Development of publication materials',
                                       description='e.g. teaching cases'))

    db.session.add(PublicationCategory(category='Non-print materials',
                                       description='film strips, films, videotapes and '
                                                   'computer software relevant to '
                                                   'academic field'))
    db.session.commit()

    # PatentOffice
    db.session.add(PatentOffice(name='Albania'))
    db.session.add(PatentOffice(name='Algeria'))
    db.session.add(PatentOffice(name='Andorra'))
    db.session.add(PatentOffice(name='Angola'))
    db.session.add(PatentOffice(name='Antigua and Barbuda'))
    db.session.add(PatentOffice(name='Argentina'))
    db.session.add(PatentOffice(name='Armenia'))
    db.session.add(PatentOffice(name='Australia'))
    db.session.add(PatentOffice(name='Austria'))
    db.session.add(PatentOffice(name='Azerbaijan'))
    db.session.add(PatentOffice(name='Bahamas'))
    db.session.add(PatentOffice(name='Bahrain'))
    db.session.add(PatentOffice(name='Bangladesh'))
    db.session.add(PatentOffice(name='Barbados'))
    db.session.add(PatentOffice(name='Belarus'))
    db.session.add(PatentOffice(name='Belgium'))
    db.session.add(PatentOffice(name='Belize'))
    db.session.add(PatentOffice(name='Benin'))
    db.session.add(PatentOffice(name='Bhutan'))
    db.session.add(PatentOffice(name='Bolivia (Plurinational State of)'))
    db.session.add(PatentOffice(name='Bosnia and Herzegovina'))
    db.session.add(PatentOffice(name='Botswana'))
    db.session.add(PatentOffice(name='Brazil'))
    db.session.add(PatentOffice(name='Brunei Darussalam'))
    db.session.add(PatentOffice(name='Bulgaria'))
    db.session.add(PatentOffice(name='Burkina Faso'))
    db.session.add(PatentOffice(name='Burundi'))
    db.session.add(PatentOffice(name='Cabo Verde'))
    db.session.add(PatentOffice(name='Cambodia'))
    db.session.add(PatentOffice(name='Cameroon'))
    db.session.add(PatentOffice(name='Canada'))
    db.session.add(PatentOffice(name='Central African Republic'))
    db.session.add(PatentOffice(name='Chad'))
    db.session.add(PatentOffice(name='Chile'))
    db.session.add(PatentOffice(name='China'))
    db.session.add(PatentOffice(name='Colombia'))
    db.session.add(PatentOffice(name='Comoros'))
    db.session.add(PatentOffice(name='Congo'))
    db.session.add(PatentOffice(name='Costa Rica'))
    db.session.add(PatentOffice(name="Cote d'Ivoire"))
    db.session.add(PatentOffice(name='Croatia'))
    db.session.add(PatentOffice(name='Cuba'))
    db.session.add(PatentOffice(name='Cyprus'))
    db.session.add(PatentOffice(name='Czech Republic'))
    db.session.add(PatentOffice(name="Democratic People's Republic of Korea"))
    db.session.add(PatentOffice(name='Democratic Republic of the Congo'))
    db.session.add(PatentOffice(name='Denmark'))
    db.session.add(PatentOffice(name='Djibouti'))
    db.session.add(PatentOffice(name='Dominica'))
    db.session.add(PatentOffice(name='Dominican Republic'))
    db.session.add(PatentOffice(name='Ecuador'))
    db.session.add(PatentOffice(name='Egypt'))
    db.session.add(PatentOffice(name='El Salvador'))
    db.session.add(PatentOffice(name='Equatorial Guinea'))
    db.session.add(PatentOffice(name='Eritrea'))
    db.session.add(PatentOffice(name='Estonia'))
    db.session.add(PatentOffice(name='Ethiopia'))
    db.session.add(PatentOffice(name='Fiji'))
    db.session.add(PatentOffice(name='Finland'))
    db.session.add(PatentOffice(name='France'))
    db.session.add(PatentOffice(name='Gabon'))
    db.session.add(PatentOffice(name='Gambia'))
    db.session.add(PatentOffice(name='Georgia'))
    db.session.add(PatentOffice(name='Germany'))
    db.session.add(PatentOffice(name='Ghana'))
    db.session.add(PatentOffice(name='Greece'))
    db.session.add(PatentOffice(name='Grenada'))
    db.session.add(PatentOffice(name='Guatemala'))
    db.session.add(PatentOffice(name='Guinea'))
    db.session.add(PatentOffice(name='Guinea-Bissau'))
    db.session.add(PatentOffice(name='Guyana'))
    db.session.add(PatentOffice(name='Haiti'))
    db.session.add(PatentOffice(name='Holy See'))
    db.session.add(PatentOffice(name='Honduras'))
    db.session.add(PatentOffice(name='Hungary'))
    db.session.add(PatentOffice(name='Iceland'))
    db.session.add(PatentOffice(name='India'))
    db.session.add(PatentOffice(name='Indonesia'))
    db.session.add(PatentOffice(name='Iran (Islamic Republic of)'))
    db.session.add(PatentOffice(name='Iraq'))
    db.session.add(PatentOffice(name='Ireland'))
    db.session.add(PatentOffice(name='Israel'))
    db.session.add(PatentOffice(name='Italy'))
    db.session.add(PatentOffice(name='Jamaica'))
    db.session.add(PatentOffice(name='Japan'))
    db.session.add(PatentOffice(name='Jordan'))
    db.session.add(PatentOffice(name='Kazakhstan'))
    db.session.add(PatentOffice(name='Kenya'))
    db.session.add(PatentOffice(name='Kiribati'))
    db.session.add(PatentOffice(name='Kuwait'))
    db.session.add(PatentOffice(name='Kyrgyzstan'))
    db.session.add(PatentOffice(name='Lao People\'s Democratic Republic'))
    db.session.add(PatentOffice(name='Latvia'))
    db.session.add(PatentOffice(name='Lebanon'))
    db.session.add(PatentOffice(name='Lesotho'))
    db.session.add(PatentOffice(name='Liberia'))
    db.session.add(PatentOffice(name='Libya'))
    db.session.add(PatentOffice(name='Liechtenstein'))
    db.session.add(PatentOffice(name='Lithuania'))
    db.session.add(PatentOffice(name='Luxembourg'))
    db.session.add(PatentOffice(name='Madagascar'))
    db.session.add(PatentOffice(name='Malawi'))
    db.session.add(PatentOffice(name='Malaysia'))
    db.session.add(PatentOffice(name='Maldives'))
    db.session.add(PatentOffice(name='Mali'))
    db.session.add(PatentOffice(name='Malta'))
    db.session.add(PatentOffice(name='Mauritania'))
    db.session.add(PatentOffice(name='Mauritius'))
    db.session.add(PatentOffice(name='Mexico'))
    db.session.add(PatentOffice(name='Monaco'))
    db.session.add(PatentOffice(name='Mongolia'))
    db.session.add(PatentOffice(name='Montenegro'))
    db.session.add(PatentOffice(name='Morocco'))
    db.session.add(PatentOffice(name='Mozambique'))
    db.session.add(PatentOffice(name='Myanmar'))
    db.session.add(PatentOffice(name='Namibia'))
    db.session.add(PatentOffice(name='Nauru'))
    db.session.add(PatentOffice(name='Nepal'))
    db.session.add(PatentOffice(name='Netherlands'))
    db.session.add(PatentOffice(name='New Zealand'))
    db.session.add(PatentOffice(name='Nicaragua'))
    db.session.add(PatentOffice(name='Niger'))
    db.session.add(PatentOffice(name='Nigeria'))
    db.session.add(PatentOffice(name='Niue'))
    db.session.add(PatentOffice(name='Norway'))
    db.session.add(PatentOffice(name='Oman'))
    db.session.add(PatentOffice(name='Pakistan'))
    db.session.add(PatentOffice(name='Palau'))
    db.session.add(PatentOffice(name='Panama'))
    db.session.add(PatentOffice(name='Papua New Guinea'))
    db.session.add(PatentOffice(name='Paraguay'))
    db.session.add(PatentOffice(name='Peru'))
    db.session.add(PatentOffice(name='Philippines'))
    db.session.add(PatentOffice(name='Poland'))
    db.session.add(PatentOffice(name='Portugal'))
    db.session.add(PatentOffice(name='Qatar'))
    db.session.add(PatentOffice(name='Republic of Korea'))
    db.session.add(PatentOffice(name='Republic of Moldova'))
    db.session.add(PatentOffice(name='Romania'))
    db.session.add(PatentOffice(name='Russian Federation'))
    db.session.add(PatentOffice(name='Rwanda'))
    db.session.add(PatentOffice(name='Saint Kitts and Nevis'))
    db.session.add(PatentOffice(name='Saint Lucia'))
    db.session.add(PatentOffice(name='Saint Vincent and the Grenadines'))
    db.session.add(PatentOffice(name='Samoa'))
    db.session.add(PatentOffice(name='San Marino'))
    db.session.add(PatentOffice(name='Sao Tome and Principe'))
    db.session.add(PatentOffice(name='Saudi Arabia'))
    db.session.add(PatentOffice(name='Senegal'))
    db.session.add(PatentOffice(name='Serbia'))
    db.session.add(PatentOffice(name='Seychelles'))
    db.session.add(PatentOffice(name='Sierra Leone'))
    db.session.add(PatentOffice(name='Singapore'))
    db.session.add(PatentOffice(name='Slovakia'))
    db.session.add(PatentOffice(name='Slovenia'))
    db.session.add(PatentOffice(name='Solomon Islands'))
    db.session.add(PatentOffice(name='Somalia'))
    db.session.add(PatentOffice(name='South Africa'))
    db.session.add(PatentOffice(name='Spain'))
    db.session.add(PatentOffice(name='Sri Lanka'))
    db.session.add(PatentOffice(name='Sudan'))
    db.session.add(PatentOffice(name='Suriname'))
    db.session.add(PatentOffice(name='Swaziland'))
    db.session.add(PatentOffice(name='Sweden'))
    db.session.add(PatentOffice(name='Switzerland'))
    db.session.add(PatentOffice(name='Syrian Arab Republic'))
    db.session.add(PatentOffice(name='Tajikistan'))
    db.session.add(PatentOffice(name='Thailand'))
    db.session.add(PatentOffice(name='the former Yugoslav Republic of Macedonia'))
    db.session.add(PatentOffice(name='Timor-Leste'))
    db.session.add(PatentOffice(name='Togo'))
    db.session.add(PatentOffice(name='Tonga'))
    db.session.add(PatentOffice(name='Trinidad and Tobago'))
    db.session.add(PatentOffice(name='Tunisia'))
    db.session.add(PatentOffice(name='Turkey'))
    db.session.add(PatentOffice(name='Turkmenistan'))
    db.session.add(PatentOffice(name='Tuvalu'))
    db.session.add(PatentOffice(name='Uganda'))
    db.session.add(PatentOffice(name='Ukraine'))
    db.session.add(PatentOffice(name='United Arab Emirates'))
    db.session.add(PatentOffice(name='United Kingdom'))
    db.session.add(PatentOffice(name='United Republic of Tanzania'))
    db.session.add(PatentOffice(name='United States of America'))
    db.session.add(PatentOffice(name='Uruguay'))
    db.session.add(PatentOffice(name='Uzbekistan'))
    db.session.add(PatentOffice(name='Vanuatu'))
    db.session.add(PatentOffice(name='Venezuela (Bolivarian Republic of)'))
    db.session.add(PatentOffice(name='Viet Nam'))
    db.session.add(PatentOffice(name='Yemen'))
    db.session.add(PatentOffice(name='Zambia'))
    db.session.add(PatentOffice(name='Zimbabwe'))
    db.session.add(PatentOffice(name='OAPI'))
    db.session.add(PatentOffice(name='ARIPO'))
    db.session.add(PatentOffice(name='ASBU'))
    db.session.add(PatentOffice(name='BOIP'))
    db.session.add(PatentOffice(name='EAPO'))
    db.session.add(PatentOffice(name='EPO'))
    db.session.add(PatentOffice(name='EUIPO'))
    db.session.add(PatentOffice(name='UPOV'))
    db.session.add(PatentOffice(name='ICPIP'))
    db.session.add(PatentOffice(name='GCC Patent Office'))
    db.session.commit()

    # PatentStatus
    db.session.add(PatentStatus(status='Patent Issued'))
    db.session.add(PatentStatus(status='Patent Pending'))
    db.session.commit()

if __name__ == '__main__':
    manager.run()

