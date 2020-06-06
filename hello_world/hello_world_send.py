#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

# hello queue to which the message will be delivered
channel.queue_declare(queue='hello')

# send message (in body) using existing queue and it always needs to go through an exchange
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")

# closinf the connection
connection.close()