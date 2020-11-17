from ..common import db
from . import Column, Integer, String


class MessageModel(db.Model):
    __tablename__ = 'messages'
    ID = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    text = Column(String, nullable=False)
    file_name = Column(String, nullable=True)
    file_type = Column(String, nullable=True)
    time = Column(String, nullable=False)

