import datetime

from sqlalchemy import Column, Integer, VARCHAR, DATE, ForeignKey

from .base import BaseModel

class User(BaseModel):
    __tablename__ = "users"

    # Телеграм user_id
    user_id = Column(Integer, unique=True, nullable=False, primary_key=True)
    username =Column(VARCHAR(32), unique=False, nullable=True)
    reg_date = Column(DATE, default=datetime.date.today())
    upd_date = Column(DATE, onupdate=datetime.date.today())

    def __str__(self) -> str:
        return f"<User:{self.user_id}>"

class User_message(BaseModel):
    __tablename__ = "user_messages"

    message_id = Column(Integer, nullable=False, primary_key=True)
    reg_date = Column(DATE, default=datetime.date.today())
    text_message = Column(VARCHAR(300), nullable=False)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)

    def __str__(self) -> str:
        return f"<User_message:{self.message_id}>"


