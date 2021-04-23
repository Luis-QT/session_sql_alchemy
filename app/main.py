""" File to init FastAPI """
import time
from fastapi import FastAPI
from fastapi import Depends
from sqlalchemy.orm import Session
from app.connections.conn_psql import get_db, refresh_db

app = FastAPI(
    docs_url="/docs",
    redoc_url="/redocs",
    title="SQL Alchemy APIs",
    description="This WEB documentates the APIs SQL Alchemy.",
    version="1.0",
    openapi_url="/openapi.json"
)

@app.get("/")
def root():
    """ Shows homepage """
    return {"Hola Mundo"}

@app.get("/db_global_flush")
def db_global_flush():
    """ Get all users """
    from db_psql.models import User
    from app.connections.conn_psql import db_global as db
    user = User(
        name='PEDRO'
    )
    db.add(user)
    db.flush()
    time.sleep(30)
    return "PEDRO No deberia estar creado"

@app.get("/solapar_commit")
def solapar_commit():
    from db_psql.models import User, Role, UserRole
    db.commit()
    return "Revisa en la DB que no deba existir PEDRO 1"


@app.get("/db_request_flush")
def db_request_flush(db: Session = Depends(get_db)):
    """ Get all users """
    from db_psql.models import User
    user = User(
        name='PEDRO'
    )
    db.add(user)
    db.flush()
    time.sleep(30)
    return "PEDRO No deberia estar creado"

@app.get("/utilitarios/refresh_db")
def refresh_db_aaa():
    """ Reset models and seeders """
    refresh_db()
    return "DB refreshed"
