# Python REST Logger
This project is a simple web server build using Python and Flask Framework which 
reads a message from an API and logs it to rabbit.

This server is intended to be used in conjunction with my ELK stack project.

## RabbitMQ
To run a stateless rabbitMQ server use the following command
``` bash
docker run --rm --name rabbitmq -d -p 5672:5672 -p 15672:15672 rabbitmq:management
``