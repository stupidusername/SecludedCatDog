from createapp import db
from sqlalchemy_utils.types.json import JSONType


class Search(db.Model):
    """
    Search model.
    """

    # Columns.
    param = db.Column('param', db.String(), primary_key=True)
    create_datetime = \
        db.Column('create_datetime', db.DateTime(), nullable=False)
    identity = db.Column('identity', JSONType, nullable=False)
