from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base, Session

class ShoppingList(Base):
    __tablename__ = 'shopping_lists'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User")

    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def save(self):
        session = Session()
        session.add(self)
        session.commit()

    @staticmethod
    def get_all():
        session = Session()
        return session.query(ShoppingList).all()