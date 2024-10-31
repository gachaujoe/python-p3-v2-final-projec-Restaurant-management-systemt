from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base


class Customer(Base):
    __tablename__ = 'customers'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True)
    phone = Column(String(15))
    
    # Relationship with orders
    orders = relationship('Order', back_populates='customer')
    
    def __repr__(self):
        return f"<Customer {self.name}>"