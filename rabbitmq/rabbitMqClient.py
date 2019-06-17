import pika

host_name="localhost"
queue_name="hello"
routing_key_name="hello"

def init():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=host_name))
    channel = connection.channel()

    channel.queue_declare(queue=queue_name)
    return connection

def send():
    connection = init()

    connection.channel().basic_publish(exchange='', routing_key=routing_key_name, body='Hello World!')
    print(" [x] Sent 'Hello World!'")
    connection.close()

def receive():
    connection = init()
    channel = connection.channel()

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)
        return body

    channel.basic_consume(
        queue=queue_name, on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
