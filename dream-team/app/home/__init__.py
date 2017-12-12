# app/home/__init__.py

from flask import Blueprint

home = Blueprint('home', __name__, template_folder='templates')

from . import views