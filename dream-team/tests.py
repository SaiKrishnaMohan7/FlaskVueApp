# tests.py

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
            SQLALCHEMY_DATABASE_URI='mysql://dt_admin:dt2016@localhost/dreamteam_test'
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

        self.assertEqual(Department.query.count(), 1)
        

if __name__ == '__main__':
    unittest.main()