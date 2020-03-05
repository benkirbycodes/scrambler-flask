from sqlalchemy import Column
from sqlalchemy.types import Integer, Text, String


class Sentence(db.Model):
    id = Column(Integer, primary_key=True, nullable=False, auto_increment=True)
    text = Column(String(120), nullable=False)
