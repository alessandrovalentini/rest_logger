from flask import Flask
from rest import requests
from logger import default_logger


app = Flask(__name__)

@app.route('/<arg>')
def home(arg):
    user = requests.getQueryParam('user')
    logger =  default_logger.simpleLogger()
    logger.warn("Request on " + arg)
    return user


@app.route('/hello')
def index():
    return "Hello, World!"

# http://localhost:5000/ciao?user=asasf