from sqlalchemy import Column
from sqlalchemy.types import Integer, Text, String


class StorySentence(db.Model):
    id = Column(Integer, primary_key=True, nullable=False, auto_increment=True)
    sentenceId = Column(Integer, nullable=False, ForeignKey('sentence.id'))
    storyId = Column(Integer, nullable=False, ForeignKey('story.id'))
