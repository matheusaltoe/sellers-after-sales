from fastapi.routing import APIRouter
from fastapi import FastAPI, Request
from schema import MessageSchema, SchedulerSchema
from database import SessionLocal, engine
from models import Customer, Scheduler, Channel, Base
import logging
import json
from database import SessionLocal

db = SessionLocal()

from logging.config import dictConfig
from log_conf import log_config
dictConfig(log_config)
logger = logging.getLogger('foo-logger')

itemrouter = APIRouter()

# def get_session():
#     session = SessionLocal()
#     try:
#         yield session
#     finally:
#         session.close()

router = APIRouter()

@router.post("/scheduler/communication")
async def post_communication(payload: SchedulerSchema, request: Request):
    print(payload.date_hour)
    request.app.pika_client.send_message(
        {
            "date_hour": str(payload.date_hour),
            "message": payload.message,
            "status_send": payload.status_send,
            "customer_id": payload.customer_id,
            "channel_id": payload.channel_id
        }
    )
    return {"message": "done"}


@router.get("/scheduler/communication")
async def read_communication():
    result = db.query(Scheduler).all()
    return result


@router.delete("/scheduler/communication/{communication_id}")
async def delete_communication(communication_id: int):
    result = db.query(Scheduler).filter_by(id=communication_id).one()
    db.delete(result)
    db.commit()
    return {"message": "done"}
