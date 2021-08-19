from pydantic import BaseModel
from datetime import datetime

class MessageSchema(BaseModel):
    description: str

class SchedulerSchema(BaseModel):
    date_hour: datetime
    message: str
    status_send: bool
    customer_id: int
    channel_id: int

class CustomerSchema(BaseModel):
    name: str
    email: str
    phone: str   

class ChannelSchema(BaseModel):
    id: int 
    description: str   