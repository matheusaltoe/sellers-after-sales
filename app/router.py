import logging
import json

from fastapi import FastAPI, Request
from fastapi.routing import APIRouter
from database import SessionLocal, engine
from log_conf import log_config
from logging.config import dictConfig
from models import Customer, Scheduler, Channel
from schema import SchedulerSchema

dictConfig(log_config)
logger = logging.getLogger('app-logger')

def get_db():
    try:
        db = SessionLocal()
        yield db 
    finally:
        db.close()

router = APIRouter()


@router.post("/scheduler/communication")
async def post_communication(payload: SchedulerSchema, request: Request):
    request.app.pika_client.send_message(
        {
            "date_hour": str(payload.date_hour),
            "message": payload.message,
            "status_send": payload.status_send,
            "customer_id": payload.customer_id,
            "channel_id": payload.channel_id
        }
    )
    return {"message": "success"}


@router.get("/scheduler/communication")
async def read_communication():
    result = db.query(Scheduler).all()
    return result


@router.delete("/scheduler/communication/{communication_id}")
async def delete_communication(communication_id: int):
    result = db.query(Scheduler).filter_by(id=communication_id).one()
    db.delete(result)
    db.commit()
    return {"message": "success"}
