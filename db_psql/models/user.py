""" User model """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from db_psql.base import BasePsql
from db_psql.mixins.guid_mixin import GuidMixin
from db_psql.mixins.timestamp_mixin import TimestampMixin

class User(BasePsql, GuidMixin, TimestampMixin):
    """ The users table """
    __tablename__ = 'users'
    name = Column(String, nullable=False)

    roles = relationship("UserRole", back_populates="user")
