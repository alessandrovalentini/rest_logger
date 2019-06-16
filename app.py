from flask import Flask
import logging
from rest import requests

app = Flask(__name__)

@app.route('/<arg>')
def home(arg):
    user = requests.getQueryParam('user')
    #setupLogger()
    logger = logging.getLogger()
    logger.warn("Request on " + arg)
    return user


@app.route('/hello')
def index():
    return "Hello, World!"


def setupLogger():
    logging.basicConfig(
        level=logging.WARN,
        format="%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s",
        handlers=[
            logging.StreamHandler()
        ])