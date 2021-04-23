""" Role model """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from db_psql.base import BasePsql
from db_psql.mixins.guid_mixin import GuidMixin
from db_psql.mixins.timestamp_mixin import TimestampMixin

class Role(BasePsql, GuidMixin, TimestampMixin):
    """ The roles table """
    __tablename__ = 'roles'
    name = Column(String, nullable=False)

    users = relationship("UserRole", back_populates="role")
