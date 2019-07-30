import pika

class RabbitMqClient:

    def __init__(self, host_name, queue_name, routing_key_name):
        self.host_name = host_name
        self.queue_name = queue_name
        self.routing_key_name = routing_key_name

    def build(self):
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=self.host_name))
        channel = connection.channel()

        channel.queue_declare(queue=self.queue_name)
        return connection

    def send(self):
        connection = self.build()

        connection.channel().basic_publish(exchange='', routing_key=self.routing_key_name, body='Hello World!')
        print(" [x] Sent 'Hello World!'")
        connection.close()

    def receive(self):
        connection = self.build()
        channel = connection.channel()

        print(" [*] Starting consumer receive")

        def callback(ch, method, properties, body):
            print(" [x] Received %r" % body)
            return body

        channel.basic_consume(consumer_callback=callback, queue=self.queue_name)

        print(' [*] Waiting for messages. To exit press CTRL+C')
        channel.start_consuming()
