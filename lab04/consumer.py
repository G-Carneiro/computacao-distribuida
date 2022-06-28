from pika import BlockingConnection, ConnectionParameters


def callback(ch, method, properties, body):
    print(f"Received: '{body.decode()}'")


queue = "producer_consumer_queue"
connection = BlockingConnection(ConnectionParameters(host="localhost"))

channel = connection.channel()

channel.queue_declare(queue=queue)

channel.basic_consume(queue=queue,
                      auto_ack=True,
                      on_message_callback=callback)

print("Waiting for messages...")
channel.start_consuming()
