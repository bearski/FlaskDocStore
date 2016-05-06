# project/user/views.py


#################
#### imports ####
#################
import datetime

from flask import render_template, Blueprint, url_for, redirect, flash, request
from flask.ext.login import login_user, logout_user, login_required, current_user

from project.models import User
from project.email import send_email
from project import db, bcrypt
from .forms import LoginForm, RegisterForm, ChangePasswordForm, EditPersonalForm
from project.token import generate_confirmation_token, confirm_token
from project.decorators import check_confirmed


################
#### config ####
################

user_blueprint = Blueprint('user', __name__,)


################
#### routes ####
################

@user_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)

    if form.validate_on_submit():
        user = User(
            email=form.email.data,
#            username=form.username.data,
            password=form.password.data,
            confirmed=False
        )
        db.session.add(user)
        db.session.commit()

        token = generate_confirmation_token(user.email)
        confirm_url = url_for('user.confirm_email', token=token, _external=True)
        html = render_template('user/activate.html', confirm_url=confirm_url)
        subject = "Please confirm your email"
        send_email(user.email, subject, html)

        login_user(user)
        flash('You registered and are now logged in. Welcome!', 'success')

        return redirect(url_for('user.unconfirmed'))

    return render_template('user/register.html', form=form)


@user_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user and bcrypt.check_password_hash(
                user.password, request.form['password']):
            login_user(user)
            flash('Welcome.', 'success')
            return redirect(url_for('main.home'))
            #return redirect(url_for('user.profile', username=user.username))
        else:
            flash('Invalid email and/or password.', 'danger')
            return render_template('user/login.html', form=form)

    return render_template('user/login.html', form=form)


@user_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You were logged out.', 'success')
    return redirect(url_for('user.login'))


@user_blueprint.route('/changepassword', methods=['GET', 'POST'])
@login_required
@check_confirmed
def changepassword():
    user = User.query.filter_by(email=current_user.email).first()
    if not user:
        flash('Password successfully changed.', 'success')
        return redirect(url_for('user.logout'))

    form = ChangePasswordForm(request.form, prefix='pwd')
    if form.validate_on_submit():
        user = User.query.filter_by(email=current_user.email).first()
        if user:
            user.password = bcrypt.generate_password_hash(form.password.data)
            db.session.commit()
            flash('Password successfully changed.', 'success')
            #return redirect(url_for('user.profile', username=user.username))
            return redirect(url_for('main.home'))
        else:
            flash('Password change was unsuccessful.', 'danger')
            return redirect(url_for('user.changepassword'))

    return render_template('user/changepassword.html', form=form)


@user_blueprint.route('/confirm/<token>')
@login_required
def confirm_email(token):
    try:
        email = confirm_token(token)
    except:
        flash('The confirmation link is invalid or has expired.', 'danger')

    user = User.query.filter_by(email=email).first_or_404()

    if user.confirmed:
        flash('Account already confirmed. Please login.', 'success')
    else:
        user.confirmed = True
        user.confirmed_on = datetime.datetime.now()
        db.session.add(user)
        db.session.commit()
        flash('You have confirmed your account. Thanks!', 'success')

    return redirect(url_for('main.home'))


@user_blueprint.route('/unconfirmed')
@login_required
def unconfirmed():
    if current_user.confirmed:
        return redirect('main.home')
    flash('Please confirm your account!', 'warning')
    return render_template('user/unconfirmed.html')

@user_blueprint.route('/resend')
@login_required
def resend_confirmation():
    token = generate_confirmation_token(current_user.email)
    confirm_url = url_for('user.confirm_email', token=token, _external=True)
    html = render_template('user/activate.html', confirm_url=confirm_url)
    subject = "Please confirm your email"
    send_email(current_user.email, subject, html)
    flash('A new confirmation email has been sent.', 'success')
    return redirect(url_for('user.unconfirmed'))


# @user_blueprint.route('/dashboard')
# @login_required
# def dashboard():
#     user = User.query.filter_by(email=current_user.email).first_or_404()
#
#     if not user:
#         flash('User not found', 'danger')
#         return redirect(url_for('main.home'))
#
#     data = {
#         "username" : user.username,
#         "firstname" : user.firstname,
#         "lastname" : user.surname,
#         "email" : user.email
#     }
#
#     return render_template('user/dashboard.html', data=data)


@user_blueprint.route('/user/<username>')
@login_required
def profile(username):
    user = User.query.filter_by(username=username).first()
    if user == None:
        flash('User %s not found.' % username, 'danger')
        return redirect(url_for('main.home'))

    return render_template('user/profile.html', user=user)


@user_blueprint.route('/edit/<username>', methods=['GET', 'POST'])
def editpersonalinfo(username):
    form = EditPersonalForm(request.form, prefix='edit')

    user = User.query.filter_by(username=username).first()
    if user == None:
        flash('User %s not found.' % username, 'danger')
        return redirect(url_for('main.home'))

    if request.method == 'POST' and form.validate_on_submit():
        user.firstname = form.firstname.data
        user.surname = form.lastname.data
        user.birthdate = form.birthdate.data
        user.gender = form.gender.data
        db.session.commit()

        return redirect(url_for('user.profile', username=username))

    return render_template('user/form.html', form=form)

@user_blueprint.route('/user_edit_firstname',methods=['GET', 'POST'])
def user_edit_firstname():
    user = User.query.filter_by(email=current_user.email).first()
    user.firstname = request.form["value"]
    db.session.commit()
    return redirect(url_for('user.profile', username=user.username))
