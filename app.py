from flask import Flask
from rest import requests
from logger import default_logger
from rabbitmq import send
from rabbitmq import receive
from rabbitmq import rabbitMqClient

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

@app.route('/send')
def writeToQueue():
    rabbitMqClient.send()
    rabbitMqClient.send()
    rabbitMqClient.send()
    #receive.receive()
    return "message sent!"

@app.route('/receive')
def readFromQueue():
    rabbitMqClient.receive()
    return "message received"

# http://localhost:5000/ciao?user=asasf