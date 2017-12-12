# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

from config import app_config

# DB object
db = SQLAlchemy()

#login object
login_manager = LoginManager()

""" 
Loads the correct config when passed a name
loads from instance/config.py as well
db object interacts with the DB
"""
def create_app(config_name):
    app = Flask(__name__, instance_relative_config = True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)

    login_manager.init_app(app)
    login_manager.login_message = 'Login to access this page'
    login_manager.login_view = 'auth_login'

    #for Migrations
    migrate = Migrate(app, db)
    from app import models

    #Registering all the Blueoprints
    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)
    
    return app

#url_prefix -> all views in the admin blueprint will be accessed through this /admin