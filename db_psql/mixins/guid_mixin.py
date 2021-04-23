""" guid_mixin.py """
import uuid
import sqlalchemy
from sqlalchemy.dialects.postgresql import UUID

class GuidMixin:
    """ Mixin Class that add a UUID id column """
    id = sqlalchemy.Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )
