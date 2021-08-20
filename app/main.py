import asyncio
import logging
from database import SessionLocal
from fastapi import FastAPI
from log_conf import log_config
from logging.config import dictConfig
from models import Scheduler
from pika_client import PikaClient
from router import router
from fastapi import FastAPI, Request

dictConfig(log_config)
logger = logging.getLogger('app-logger')

db = SessionLocal()

class SellerApp(FastAPI):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pika_client = PikaClient(self.incoming_message)

    @classmethod
    def incoming_message(cls, message: dict):
        db_scheduler = Scheduler(
            **message
        )
        try:
            db.add(db_scheduler)
            db.commit()
        except:
            db.rollback()

app = SellerApp()
app.include_router(router, prefix='/api/v1')


@app.on_event('startup')
async def startup():
    loop = asyncio.get_running_loop()
    task = loop.create_task(app.pika_client.consume(loop))
    await task        
