# app/admin/views.py

from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from . import admin
from forms import DepartmentForm
from .. import db
from ..models import Department

def check_admin():
    """
    Give only Admin user access to add Departments
    """

    if not current_user.is_admin:
        abort(403, description='Forbidden! You do not have permissions')

# Setup Admin views

@admin.route('/departments', methods=['GET', 'POST'])
@login_required
def list_departments():
    """ 
    List all departments
    """
    check_admin()

    departments = Department.query.all()

    return render_template('admin/departments/departments.html',
                           departments=departments, title="Departments")

@admin.route('/departments/add', methods=['GET' ,'POST'])
@login_required
def add_department():
    """ 
    Add a Department
    """
    
    add_department = True

    form = DepartmentForm()
    if form.validate_on_submit():
        department = Department(name=form.name.data, description=form.description.data)

        try:
            # add department to db
            db.session.add(department)
            db.session.commit()
            flash('Department Added Successfully')
        except:
            flash('Error: Department exists')
        
        # Redirect to /departments
        return redirect(url_for('admin.list_departments'))

    # Load department template
    return render_template('admin/departments/departments.html', action ='Add',
                            add_department = add_department, form = form,
                            title ='Add Department')


@admin.route('/departments/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_department(id):
    """
    Edit a department
    """

    check_admin()

    add_department = False

    department = Department.query.get_or_404(id)
    form = DepartmentForm(obj = department)
    if form.validate_on_submit():
        department.name = form.name.data
        department.description = form.description.data
        db.session.commit()
        flash('Changes to ' + department.name + ' have been made')

        # redirect to /departments
        return redirect(url_for('admin.list_departments'))
    
    form.description.data = department.description
    form.name.data = department.name

    return render_template('admin/departments/department.html', action ='Edit',
                            add_department = add_department, form = form,
                            department=department, title='Edit Department')

@admin.route('/departments/delete/<int:id>')
@login_required
def delete_department(id):
    """ 
    Delete a department
    """

    check_admin()

    department = Department.query.get_or_404(id)
    db.session.delete(department)
    db.session.commit()
    flash('Department has been deleted')

    # redirect to /departments
    return redirect(url_for('admin.list_departments'))

    return render_template(title='Delete Department')
