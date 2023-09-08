from sqlalchemy import Column, Integer, String
from database import Base, Session

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name

    def save(self):
        session = Session()
        session.add(self)
        session.commit()

    @staticmethod
    def get_by_id(user_id):
        session = Session()
        return session.query(User).get(user_id)