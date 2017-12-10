#app/views.py
#Contains all the routes, tells Flask what to display on what path

from flask import render_template
from app import app

#decorator
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

#render_template returns TemplateNotFound if no template