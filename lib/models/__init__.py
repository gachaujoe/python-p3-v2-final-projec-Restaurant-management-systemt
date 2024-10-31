# import sqlite3

# CONN = sqlite3.connect('company.db')
# CURSOR = CONN.cursor()

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from .customer import Customer
from .menu_item import MenuItem
from .order import Order
from .session import session

# database engine
engine = create_engine('sqlite:///restaurant.db')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()