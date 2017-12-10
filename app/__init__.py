#app/__init__.py

from flask import Flask

#Initialize App
app = Flask(__name__, instance_relative_config = True)

#Load Views
from app import views

#Load Config file
#This is Possible by instance_relative_config = True
app.config.from_object('config')