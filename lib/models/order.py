from sqlalchemy import Column, Integer, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base

class Order(Base):
    __tablename__ = 'orders'
    
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    menu_item_id = Column(Integer, ForeignKey('menu_items.id'))
    quantity = Column(Integer, default=1)
    total_price = Column(Float)
    order_date = Column(DateTime, default=datetime.now)
    
    # Relationships
    customer = relationship('Customer', back_populates='orders')
    menu_item = relationship('MenuItem', back_populates='orders')
    
    def __repr__(self):
        return f"<Order {self.id} - Customer: {self.customer.name}>"