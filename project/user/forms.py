# project/user/forms.py


from flask_wtf import Form
from wtforms import (StringField, PasswordField, SelectField, FieldList,
    FormField, TextAreaField
)
from wtforms.validators import DataRequired, Email, Length, EqualTo, Optional
from wtforms.fields.html5 import DateField

from project.models import User


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


gender = [
    (''),
    ('Female'),
    ('Male')
]


class EditPersonalForm(Form):
    firstname = StringField('firstname', validators=[Optional()])
    lastname = StringField('lastname', validators=[Optional()])
    # birthdate = StringField('birthdate', validators=[Optional()])
    birthdate = DateField('birthdate', format('%Y-%m-%d'))
    gender = SelectField('gender', choices=gender)


class EmploymentForm(Form):
    id = StringField('id', validators=[DataRequired()])
    human_id = StringField('human_id', validators=[Optional()])
    employer = StringField('employer', validators=[Optional()])
    position = StringField('position', validators=[Optional()])
    start_date = DateField('start_date', validators=[Optional()])
    end_date = DateField('end_date', validators=[Optional()])
    job_desc = TextAreaField('job_desc', validators=[Optional()])


class EmploymentListForm(Form):
    employmentlist = FieldList(FormField(EmploymentForm))


class EducationForm(Form):
    human_id = StringField('human_id', validators=[Optional()])
    educational_institution = StringField('educational_institution', validators=[Optional()])
    course_studied = StringField('course_studied', validators=[Optional()])
    # start_date = DateField('DatePicker', format('%Y-%m-%d'))
    # end_date = DateField('DatePicker', format('%Y-%m-%d'))
    accolades = TextAreaField('accolades', validators=[Optional()])