from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Scheduler(Base):
    __tablename__ = "scheduler"

    id = Column(Integer, primary_key=True, autoincrement=True)
    date_hour = Column(DateTime)
    message = Column(String)
    status_send = Column(Boolean)

    customer_id = Column(Integer, ForeignKey('customer.id'))
    custom = relationship('Customer', back_populates='owner')
    channel_id = Column(Integer, ForeignKey('channel.id'))
    chann = relationship('Channel', back_populates='sch')

class Customer(Base):    
    __tablename__ = "customer"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    phone = Column(String)

    owner = relationship("Scheduler", back_populates="custom")

class Channel(Base):
    __tablename__ = "channel"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String, unique=True)

    sch = relationship('Scheduler', back_populates='chann')
