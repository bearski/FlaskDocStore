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
from wtforms.widgets import HTMLString, html_params
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from project.models import User, EducationalInstitutionType, Gender


class DatePickerWidget(object):
    """
    Date Time picker from Eonasdan GitHub
    """
    data_template = ('<div class="input-group date appbuilder_date" id="datepicker">'
                    '<span class="input-group-addon"><i class="fa fa-calendar cursor-hand"></i>'
                    '</span>'
                    '<input class="form-control" data-format="yyyy-MM-dd" %(text)s/>'
                    '</div>'
                    )

    def __call__(self, field, **kwargs):
        kwargs.setdefault('id', field.id)
        kwargs.setdefault('name', field.name)
        if not field.data:
            field.data = ""
        template = self.data_template

        return HTMLString(template % {'text': html_params(type='text',
                                      value=field.data,
                                      **kwargs)
                                      })

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
    educational_institution_type = StringField('educational_institution_type',
                                          validators=[Optional()])
    course_studied = StringField('course_studied', validators=[Optional()])
    start_date = DateField('start_date', validators=[Optional()])
    end_date = DateField('end_date', validators=[Optional()])
    accolades = TextAreaField('accolades', validators=[Optional()])
    educational_institution_type_list = QuerySelectField(query_factory=
                                                         EducationalInstitutionTypes,
                                                         allow_blank=True)


class EducationFormListForm(Form):
    educationlist = FieldList(FormField(EducationForm))