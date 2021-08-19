import os
from os import environ
from sqlalchemy import create_engine, orm
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

POSTGRES_USER = environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = environ.get("POSTGRES_PASSWORD")
POSTGRES_SERVER = environ.get("POSTGRES_HOST")
POSTGRES_PORT = environ.get("POSTGRES_PORT")
POSTGRES_DB = environ.get("POSTGRES_DATABASE")

#SQLALCHEMY_DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@docker_db_1:{POSTGRES_PORT}/{POSTGRES_DB}"
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/teste"
#SQLALCHEMY_DATABASE_URL = os.getenv("DB_CONN")

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal =  sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base = declarative_base()
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

