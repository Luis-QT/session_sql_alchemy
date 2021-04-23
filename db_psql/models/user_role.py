""" UserRole model """
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from db_psql.base import BasePsql
from db_psql.mixins.guid_mixin import GuidMixin
from db_psql.mixins.timestamp_mixin import TimestampMixin

class UserRole(BasePsql, GuidMixin, TimestampMixin):
    """ The user roles table """
    __tablename__ = 'user_roles'
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    role_id = Column(UUID(as_uuid=True), ForeignKey('roles.id'))

    user = relationship("User", back_populates="roles")
    role = relationship("Role", back_populates="users")
