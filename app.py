from flask import Flask
from rest import requests
from logger import default_logger
from logger import rabbit_logger
from rabbitmq.client import RabbitMqClient
import threading


app = Flask(__name__)

rabbitMqClient = RabbitMqClient("localhost", "hello", "hello")

@app.route('/')
def index():
    rabbit_logger.print_log
    return "Hello, World!"

@app.route('/<arg>')
def home(arg):
    user = requests.getQueryParam('user')
    logger = default_logger.simpleLogger()
    logger.warn("Request on " + arg)
    return user


@app.route('/send')
def writeToQueue():
    rabbitMqClient.send()
    rabbitMqClient.send()
    rabbitMqClient.send()
    return "message sent!"

if __name__ == "__main__":
    print("starting new thread")
    threading.Thread(target=app.run).start()
    threading.Thread(target=rabbitMqClient.receive).start()

    # http://localhost:5000/ciao?user=asasf
    # http://localhost:5000/send