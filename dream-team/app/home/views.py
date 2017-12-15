from flask import render_template, abort
from flask_login import login_required, current_user

from . import home


@home.route('/')
def homepage():
    """
    Render the homepage template on the / route
    """
    return render_template('home/index.html', title="Welcome")


@home.route('/dashboard')
@login_required
def dashboard():
    """
    Render the dashboard template on the /dashboard route
    """
    return render_template('home/dashboard.html', title="Dashboard")


@home.route('/admin/dashboard')
@login_required
def admin_dashboard():
    """
    Render the admin dashboard template on the admin/dashboard route
    """
    # check id user is admin if not 403
    if not current_user.is_admin:
         abort(403, description='Forbidden! Not an admin user')

    return render_template('home/admin_dashboard.html', title="Dashboard")