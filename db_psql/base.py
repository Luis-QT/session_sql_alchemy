""" SQLAlchemy helper function """
import uuid
import enum
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from utilities import tz

class Base:
    """ Custom declarative base """
    def as_dict(self):
        """ Convert object to dictionary """
        return model_as_dict(self)

def model_as_dict(model) -> dict:
    """Convert given sqlalchemy model to dict (relationships not included)."""
    result = {}
    for attr in sqlalchemy.inspect(model).mapper.column_attrs:
        value = getattr(model, attr.key)
        if isinstance(value, (tz.datetime, tz.date)):
            value = value.isoformat()
        elif isinstance(value, uuid.UUID):
            value = str(value)
        elif isinstance(value, enum.Enum):
            value = value.name
        result[attr.key] = value
    return result

BasePsql = declarative_base(cls=Base)
Session = sessionmaker()
