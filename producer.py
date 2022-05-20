#!/usr/bin/env python
import pika
#
# # connection to rabbitmq server
# connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# channel = connection.channel()
#
# # check for queue in consumer exist
# channel.queue_declare(queue='hello')
#
# #
# channel.basic_publish(exchange='',
#                       routing_key='hello',
#                       body='Hello World!')
# print(" [x] Sent 'Hello World!'")
#
# connection.close()

with pika.BlockingConnection(pika.ConnectionParameters('localhost')) as connection:
    channel = connection.channel()

    # check for queue in consumer exist
    channel.queue_declare(queue='hello')

    #
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body='Hello World!')
    print(" [x] Sent 'Hello World!'")
