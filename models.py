from sqlalchemy import Column, Integer, String, Text
from database import Base

class Books(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    description = Column(String)
    rating = Column(Integer)

class Orders(Base):
    __tablename__ = "ORDERS_FLATTENED_V3"
    OS_ORDER_CD = Column(Text)
    OS_CUST_NAME = Column(Text)
    OS_CUST_EMAIL = Column(Text)
    OS_CUST_PHONE_NUMBER = Column(Text)
    OS_TOTAL_PRICE = Column(Integer)
    OS_ORDER_STATUS = Column(Text)
    OP_ORDER_ID = Column(Text, primary_key=True)
    OP_PROD_NAME = Column(Text)
    OP_PROD_ID = Column(Text)
    OP_PROD_PRICE = Column(Integer)
    