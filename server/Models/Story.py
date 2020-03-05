from sqlalchemy import Column
from sqlalchemy.types import Integer, Text, String


class Story(db.Model):
    id = Column(Integer, primary_key=True, nullable=False, auto_increment=True)
    title = Column(String(60), nullable=False)
