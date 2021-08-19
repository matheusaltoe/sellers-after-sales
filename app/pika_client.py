import json
import logging
import pika 
import logging
import uuid
from aio_pika import connect_robust 
from log_conf import log_config
from logging.config import dictConfig

dictConfig(log_config)
logger = logging.getLogger('app-logger')


class PikaClient:
    def __init__(self, process_callable):
        self.credentials = pika.PlainCredentials('guest', 'guest')
        self.publish_queue_name = 'scheduler_queue'
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost', credentials=self.credentials, heartbeat=0)
        )
        self.channel = self.connection.channel()
        self.publish_queue = self.channel.queue_declare(queue=self.publish_queue_name)
        self.callback_queue = self.publish_queue.method.queue
        self.response = None
        self.process_callable = process_callable
        logger.info('Pika connection initialized')

    async def consume(self, loop):
        connection = await connect_robust(host='localhost',
                                        login='guest',
                                        password='guest',
                                        port=5672,
                                        loop=loop)
        channel = await connection.channel()
        queue = await channel.declare_queue('scheduler_queue')
        await queue.consume(self.process_incoming_message, no_ack=False)
        logger.info('Established pika async listener')
        return connection

    async def process_incoming_message(self, message):
        message.ack()
        body = message.body
        logger.info('Received message')
        if body:
            self.process_callable(json.loads(body))

    def send_message(self, message: dict):
        self.channel.basic_publish(
            exchange='',
            routing_key=self.publish_queue_name,
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=str(uuid.uuid4())
            ),
            body=json.dumps(message)
        )
