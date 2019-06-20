from flask import Flask
from rest import requests
from logger import default_logger
from rabbitmq import send
from rabbitmq import receive
from rabbitmq import rabbitMqClient
import threading

app = Flask(__name__)


from threading import Thread
from time import sleep

@app.route('/')
def index():
    return "Hello, World!"

#@app.route('/<arg>')
#def home(arg):
#    user = requests.getQueryParam('user')
#    logger =  default_logger.simpleLogger()
#    logger.warn("Request on " + arg)
#    return user


@app.route('/send')
def writeToQueue():
    rabbitMqClient.send()
    rabbitMqClient.send()
    rabbitMqClient.send()
    #receive.receive()
    return "message sent!"

#@app.route('/receive')
#def readFromQueue():
#    rthreading.Thread(target=rabbitMqClient.receive).start()
#    return "start receiving messages from queue..."

if __name__ == "__main__":
    threading.Thread(target=app.run).start()
    threading.Thread(target=rabbitMqClient.receive).start()

# http://localhost:5000/ciao?user=asasf