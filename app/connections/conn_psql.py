""" File to connect PostgreSQL Database """
import os
import sqlalchemy
from db_psql import BasePsql, Session

def build_uri():
    """ Build Database URI Postgres """
    uri_psql = str("")
    if os.environ['APP_MODE'] == "development":
        uri_psql = str("postgresql://{user}:{password}@{host}:{port}/{database}").format(
            user=os.environ['POSTGRES_USER'],
            password=os.environ['POSTGRES_PASSWORD'],
            host="db_psql",
            port=os.environ['POSTGRES_PORT'],
            database=os.environ['POSTGRES_DB']
        )
    if os.environ['APP_MODE'] == "staging":
        uri_psql = str("postgresql://{user}:{password}@{host}:{port}/{database}").format(
            user=os.environ['POSTGRES_STAGING_USER'],
            password=os.environ['POSTGRES_STAGING_PASSWORD'],
            host=os.environ['POSTGRES_STAGING_HOST'],
            port=os.environ['POSTGRES_STAGING_PORT'],
            database=os.environ['POSTGRES_STAGING_DB']
        )
    return uri_psql

def refresh_db():
    """ Function that reset the database. Resets models and seeders """
    BasePsql.metadata.drop_all(bind=engine)
    BasePsql.metadata.create_all(bind=engine)

def get_db():
    """ Dependency that generates a session instance """
    db = Session(bind=engine)
    try:
        yield db
    finally:
        db.close()

engine = sqlalchemy.create_engine(build_uri())
BasePsql.metadata.create_all(bind=engine)
db_global = Session(bind=engine)
