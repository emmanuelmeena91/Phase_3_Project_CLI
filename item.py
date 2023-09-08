from sqlalchemy import Column, Integer, String, ForeignKey, Float
from database import Base

class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    shopping_list_id = Column(Integer, ForeignKey('shopping_lists.id'))

    def __init__(self, name, price, shopping_list_id):
        self.name = name
        self.price = price
        self.shopping_list_id = shopping_list_id

    def save(self, session):
        session.add(self)
        session.commit()

    @staticmethod
    def get_by_id(item_id, session):
        return session.query(Item).get(item_id)

    def delete(self, session):
        session.delete(self)
        session.commit()