from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from .base import Base

class MenuItem(Base):
    __tablename__ = 'menu_items'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(255))
    price = Column(Float, nullable=False)
    category = Column(String(50))
    
    # Relationship with orders
    orders = relationship('Order', back_populates='menu_item')
    
    def __repr__(self):
        return f"<MenuItem {self.name} - ${self.price}>"