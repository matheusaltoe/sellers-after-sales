from typing import Optional
from fastapi import FastAPI
from pika_client import PikaClient
from router import router
import asyncio
import logging
from fastapi import FastAPI, Request
import time
import logging

from logging.config import dictConfig
from log_conf import log_config
dictConfig(log_config)
logger = logging.getLogger('foo-logger')
from database import SessionLocal
from models import Scheduler

db = SessionLocal()

class FooApp(FastAPI):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pika_client = PikaClient(self.log_incoming_message)

    @classmethod
    def log_incoming_message(cls, message: dict):
        """Method to do something meaningful with the incoming message"""
        db_user = Scheduler(
            **message
        )
        db.add(db_user)
        db.commit()
        logger.info('Here we got incoming message %s', message)
time.sleep(5)
app = FooApp()
app.include_router(router, prefix='/api/v1')


@app.on_event('startup')
async def startup():
    loop = asyncio.get_running_loop()
    task = loop.create_task(app.pika_client.consume(loop))
    await task        
