import pika

def receive():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')


    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)
        return body


    channel.basic_consume(
        queue='hello', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    resp = channel.start_consuming()
    print("received " + resp )