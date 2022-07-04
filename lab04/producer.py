from random import randint

from pika import BlockingConnection, ConnectionParameters

connection = BlockingConnection(ConnectionParameters("localhost"))
channel = connection.channel()

queue = "producer_consumer_queue"
channel.queue_declare(queue=queue)

while True:
    message = input("Write a message (quit to exit): ")
    # message = "a" * randint(1, 11)
    if (message.lower() == "quit"):
        break

    channel.basic_publish(exchange="",
                          routing_key=queue,
                          body=bytes(message, "UTF-8"))
    print(f"Sent: '{message}'")
connection.close()
