# tests.py

"""
Note that each test method begins with test. This is deliberate, because unittest,
the Python unit testing framework, uses the test prefix to automatically identify test methods.
"""

import unittest
import os

from flask import abort, url_for
from flask_testing import TestCase

from app import create_app, db
from app.models import Department, Employee, Role

class TestBase(TestCase):

    def create_app(self):

        # test configurations
        config_name = 'testing'
        app = create_app(config_name)
        app.config.update(
            SQLALCHEMY_DATABASE_URI='mysql://dt_admin:dt2017@localhost/dreamteam_test'
        )
        return app

    def setUp(self):
        """
        This is called before every test
        """

        db.create_all()

        # create test user with admin privs
        admin = Employee(username='admin', password='admin2017', is_admin=True)

        # create test user non admin privs
        employee = Employee(username='test_user', password='test_2017')

        # save to db
        db.session.add(admin)
        db.session.add(employee)
        db.session.commit()

    def tearDown(self):
        """
        Called after every test
        """

        db.session.remove()
        db.drop_all()

class TestModels(TestBase):
    
    def test_employee_model(self):
        """ 
        test number of records in employee table
        """
        self.assertEqual(Employee.query.count(), 2)

    def test_department_model(self):
        """ 
        test number of records in employee table
        """
        # create a test department
        department = Department(name = 'IT', description = 'Infra Nerds')

        # save to db
        db.session.add(department)
        db.session.commit()

        self.assertEqual(Department.query.count(), 1)

    def test_role_model(self):
        """
        test number of records in role table
        """

        # create role
        role = Role(name='CEO', description = 'Run this!')

        # save to db
        db.session.add(role)
        db.session.commit()

        self.assertEqual(Role.query.count(), 1)

class TestViews(TestBase):
    
    def test_homepage(self):
        """ 
        Test: homepage access w/o login
        """

        response = self.client.get(url_for('home.homepage'))
        self.assertEqual(response.status_code, 200)
    
    def test_logout_view(self):
        """ 
        Test: logout is not accessible w/o login
        and redirect to login page then logout
        """

        target_url = url_for('auth.logout')
        redirect_url = url_for('auth.login', next = target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)

    def test_dashboard_view(self):
        """
        Test: dashboard inaccessible w/o login
        and redirect to login page then to dashboard
        """

        target_url = url_for('home.dashboard')
        redirect_url = url_for('auth.login', next = target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)

    def test_admin_dashboard(self):
        """
        Test: admin dashboard is inaccessible w/o login
        and redirects to login then admin dashboard
        """

        target_url = url_for('home.admin_dashboard')
        redirect_url = url_for('auth.login', next = target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)

    def test_department_views(self):
        """ 
        Test: Departments page inaccessible w/o login
        and redirects to login page then departments page
        """

        target_url = url_for('admin.list_departments')
        redirect_url = url_for('auth.login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)

    def test_employees_view(self):
        """
        Test: Employees page inaccessible w/o login
        and redirect to login page then employees page
        """
        target_url = url_for('admin.list_employees')
        redirect_url = url_for('auth.login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)

class TestErrorPages(TestBase):

    def test_403_forbidden(self):
        # create route to abort the request with the 500 Error
        @self.app.route('/403')
        def forbidden_error():
            abort(403)
            
        response = self.client.get('/403')
        self.assertEqual(response.status_code, 403)
        self.assertTrue('403 Error' in response.data)
    
    def test_404_not_found(self):
        response = self.client.get('/nothinghere')
        self.assertEqual(response.status_code, 404)
        self.assertTrue("404 Error" in response.data)

    def test_500_internal_server_error(self):
        # create route to abort the request with the 500 Error
        @self.app.route('/500')
        def internal_server_error():
            abort(500)

        response = self.client.get('/500')
        self.assertEqual(response.status_code, 500)
        self.assertTrue("500 Error" in response.data)

if __name__ == '__main__':
    unittest.main()