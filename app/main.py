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
from . import models

dictConfig(log_config)
logger = logging.getLogger('app-logger')

models.Base.metadata.create_all(bind=engine)

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

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.on_event('startup')
async def startup():
    loop = asyncio.get_running_loop()
    task = loop.create_task(app.pika_client.consume(loop))
    await task        
