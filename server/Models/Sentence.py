from sqlalchemy import Column
from sqlalchemy.types import Integer, Text, String


class User(db.Model):
    id = Column(Integer, primary_key=True, nullable=False)
