# project/user/forms.py


from flask_wtf import Form
from wtforms import (
    StringField,
    PasswordField,
    FieldList,
    FormField,
    TextAreaField
)

from wtforms.validators import DataRequired, Email, Length, EqualTo, Optional
from wtforms.fields.html5 import DateField
# from wtforms.widgets import HTMLString, html_params
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from project.models import (
    User,
    EducationalInstitutionType,
    Gender,
    PatentOffice,
    PatentStatus,
    PublicationCategory
)



# class DatePickerWidget(object):
#     """
#     Date Time picker from Eonasdan GitHub
#     """
#     data_template = ('<div class="input-group date appbuilder_date" id="datepicker">'
#                     '<span class="input-group-addon"><i class="fa fa-calendar cursor-hand"></i>'
#                     '</span>'
#                     '<input class="form-control" data-format="yyyy-MM-dd" %(text)s/>'
#                     '</div>'
#                     )
#
#     def __call__(self, field, **kwargs):
#         kwargs.setdefault('id', field.id)
#         kwargs.setdefault('name', field.name)
#         if not field.data:
#             field.data = ""
#         template = self.data_template
#
#         return HTMLString(template % {'text': html_params(type='text',
#                                       value=field.data,
#                                       **kwargs)
#                                       })

class LoginForm(Form):
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])


class RegisterForm(Form):
    email = StringField(
        'email',
        validators=[DataRequired(), Email(message=None), Length(min=6, max=40)])
    password = PasswordField(
        'password',
        validators=[DataRequired(), Length(min=6, max=25)]
    )
    confirm = PasswordField(
        'Repeat password',
        validators=[
            DataRequired(),
            EqualTo('password', message='Passwords must match.')
        ]
    )

    def validate(self):
        initial_validation = super(RegisterForm, self).validate()
        if not initial_validation:
            return False
        user = User.query.filter_by(email=self.email.data).first()
        if user:
            self.email.errors.append("Email already registered")
            return False
        return True


class ChangePasswordForm(Form):
    password = PasswordField(
        'password',
        validators=[DataRequired(), Length(min=6, max=25)]
    )

    confirm = PasswordField(
        'Repeat password',
        validators=[
            DataRequired(),
            EqualTo('password', message='Passwords must match.')
        ]
    )


def GenderSelect():
    return Gender.query   #.all()


class EditPersonalForm(Form):
    firstname = StringField('firstname', validators=[Optional()])
    lastname = StringField('lastname', validators=[Optional()])
    birthdate = StringField('birthdate', validators=[Optional()])
    gender_selection = StringField('gender', validators=[Optional()])
    gender = QuerySelectField(query_factory=GenderSelect, allow_blank=True)


class EmploymentForm(Form):
    id = StringField('id', validators=[Optional()])
    human_id = StringField('human_id', validators=[DataRequired()])
    employer = StringField('employer', validators=[DataRequired()])
    position = StringField('position', validators=[DataRequired()])
    start_date = DateField('start_date', validators=[Optional()])
    end_date = DateField('end_date', validators=[Optional()])
    job_desc = TextAreaField('job_desc', validators=[Optional()])


class EmploymentListForm(Form):
    employmentlist = FieldList(FormField(EmploymentForm))


def EducationalInstitutionTypes():
    return EducationalInstitutionType.query   #.all()


class EducationForm(Form):
    id = StringField('id', validators=[Optional()])
    human_id = StringField('human_id', validators=[Optional()])
    educational_institution = StringField('educational_institution',
                                          validators=[Optional()])
    course_studied = StringField('course_studied', validators=[Optional()])
    start_date = DateField('start_date', validators=[Optional()])
    end_date = DateField('end_date', validators=[Optional()])
    accolades = TextAreaField('accolades', validators=[Optional()])
    educational_institution_type = StringField('educational_institution_type',
                                               validators=[Optional()])
    educational_institution_type_list = QuerySelectField(
        query_factory=EducationalInstitutionTypes, allow_blank=True)


class EducationFormListForm(Form):
    educationlist = FieldList(FormField(EducationForm))


def PublicationCategoryList():
    return PublicationCategory.query


class PublicationForm(Form):
    id = StringField('id', validators=[Optional()])
    human_id = StringField('human_id', validators=[Optional()])
    title = StringField('human_id', validators=[Optional()])
    authors = StringField('authors', validators=[Optional()])
    publication_date = DateField('publication_date', validators=[Optional()])
    publisher = StringField('publisher', validators=[Optional()])
    publication_url = StringField('publication_url', validators=[Optional()])
    description = TextAreaField('description', validators=[Optional()])
    publication_category_list = QuerySelectField(query_factory=
                                                 PublicationCategoryList,
                                                 allow_blank=True)
    publication_category = StringField('publication_category',
                                       validators=[Optional()])


class PublicationFormListForm(Form):
    publicationlist = FieldList(FormField(PublicationForm))


def PatentOfficeList():
    return PatentOffice.query


def PatentStatusList():
    return PatentStatus.query


class PatentForm(Form):
    id = StringField('id', validators=[Optional()])
    human_id = StringField('human_id', validators=[Optional()])
    title = StringField('title', validators=[Optional()])
    description = TextAreaField('description', validators=[Optional()])
    patent_number = StringField('patent_number', validators=[Optional()])
    inventors = StringField('inventors', validators=[Optional()])
    issue_date = DateField('issue_date', validators=[Optional()])
    patent_office = StringField('patent_office', validators=[Optional()])
    patent_office_list = QuerySelectField(query_factory=PatentOfficeList,
                                          allow_blank=True)
    patent_status = StringField('patent_status', validators=[Optional()])
    patent_status_list = QuerySelectField(query_factory=PatentStatusList,
                                          allow_blank=True)
    patent_url = StringField('patent_url', validators=[Optional()])


class PatentFormListForm(Form):
    patentlist = FieldList(FormField(PatentForm))


class CertificationForm(Form):
    id = StringField('id', validators=[Optional()])
    human_id = StringField('human_id', validators=[Optional()])
    name = StringField('name', validators=[Optional()])
    certification_number = StringField('certification_number',
                                       validators=[Optional()])
    issue_date = DateField('issue_date', validators=[Optional()])
    expiry_date = DateField('expiry_date', validators=[Optional()])
    certification_url = StringField('certification_url',
                                    validators=[Optional()])