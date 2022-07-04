from time import sleep

from pika import BlockingConnection, ConnectionParameters


def callback(ch, method, properties, body):
    message: str = body.decode()
    print(f"Received: '{message}'")
    sleep(len(message))


queue = "producer_consumer_queue"
connection = BlockingConnection(ConnectionParameters(host="localhost"))

channel = connection.channel()

channel.queue_declare(queue=queue)
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue=queue,
                      auto_ack=True,
                      on_message_callback=callback)

print("Waiting for messages...")
channel.start_consuming()
