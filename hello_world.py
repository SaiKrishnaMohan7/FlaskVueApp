#flask hello_world.py

from flask import Flask

app = Flask(__name__)

#decorator
@app.route('/')
def hello_world():
    return 'Hello World'