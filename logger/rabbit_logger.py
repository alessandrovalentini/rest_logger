# https://github.com/albertomr86/python-logging-rabbitmq/

import logging
from python_logging_rabbitmq import RabbitMQHandler


def print_log():
    logger = logging.getLogger('myapp')
    logger.setLevel(logging.WARNING)

    rabbit = RabbitMQHandler(host='localhost', port=5672)
    logger.addHandler(rabbit)

    logger.warning('test debug')
