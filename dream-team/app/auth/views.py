# app/auth/views.py
""" Routes for auth """

from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user

from app.auth.forms import LoginForm, RegistrationFrom
from . import auth
from .. import db
from .. models import Employee

@auth.route('/register', methods=['GET', 'POST'])
def register():
    """
    Handle requests to /register route
    Add an employee to DB through Regitration form
    """

    form = RegistrationFrom()
    if form.validate_on_submit():
        employee = Employee(email=form.email.data,
                            username=form.username.data,
                            first_name=form.first_name.data,
                            last_name=form.last_name.data,
                            password=form.password.data)

        #add employee to db
        db.session.add(employee)
        db.session.commit()
        flash('Regitration Successful, you can now login')

        # Redirect to login page
        return redirect(url_for('auth.login'))

    # load registration template
    return render_template('auth/register.html', form=form, title='Register')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handle login requests
    Log employee in through login form
    """
    form = LoginForm()
    if form.validate_on_submit():
        
        # check wether employee exists in db and password matches
        employee = Employee.query.filter_by(email=form.email.data).first()
        if employee is not None and employee.verify_password(form.password.data):
            # log employee in
            login_user(employee)

            #check if admin user and redirect to admin dashboard if true
            if employee.is_admin:
                return redirect(url_for('home.admin_dashboard'))
            else:
                return redirect(url_for('home.dashboard'))

            # When login details are incorrect
        else:
            flash('Invalid user login or password')

    #Render Login Template
    return render_template('auth/login.html', form=form, title='Login')

@auth.route('/logout')
@login_required
def logout():
    """ 
    Handle Logout requests
    """

    logout_user()
    flash('Logout Successful')

    # redirect to login page
    return redirect(url_for('auth.login'))
    
    