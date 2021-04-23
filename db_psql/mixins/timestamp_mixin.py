""" timestamp_mixin.py """
import sqlalchemy
from sqlalchemy.ext.declarative import declared_attr
from utilities import tz

class TimestampMixin:
    """ Mixin to add update_at and created_at columns
    The columns are added at the *end* of the table
    """
    @declared_attr
    def updated_at(self):
        """ Last update timestamp """
        column = sqlalchemy.Column(
            sqlalchemy.DateTime(timezone=True),
            default=tz.utcnow,
            onupdate=tz.utcnow,
            nullable=False,
        )
        # pylint: disable=protected-access
        column._creation_order = 9800
        return column
