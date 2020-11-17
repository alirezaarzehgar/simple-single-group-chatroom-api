from ..common import db
from . import Column, Integer, String


class UserModel(db.Model):
    __tablename__ = 'users'
    ID = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    profile = Column(String, nullable=True)

