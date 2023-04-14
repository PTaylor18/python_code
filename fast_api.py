from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


class Book(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=100)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=-1, lt=101)


class Order(BaseModel):
    id: int
    OS_ORDER_CD: str
    OS_CUST_NAME: str
    OS_CUST_EMAIL: str
    OS_CUST_PHONE_NUMBER: str
    OS_TOTAL_PRICE: int
    OS_ORDER_STATUS: str
    OP_ORDER_ID: str
    OP_PROD_NAME: str
    OP_PROD_ID: str
    OP_PROD_PRICE: int


@app.get("/")
def read_api(db: Session = Depends(get_db)):
    return db.query(models.Orders).all()


# @app.get("/{order_id}")
# def get_order(order_id: str, db: Session = Depends(get_db)):


@app.post("/")
def create_order(order: Order, db: Session = Depends(get_db)):
    order_model = models.Orders()
    order_model.OS_ORDER_CD = order.OS_ORDER_CD
    order_model.OS_CUST_NAME = order.OS_CUST_NAME
    order_model.OS_CUST_EMAIL = order.OS_CUST_EMAIL
    order_model.OS_CUST_PHONE_NUMBER = order.OS_CUST_PHONE_NUMBER
    order_model.OS_TOTAL_PRICE = order.OS_ORDER_CD
    order_model.OS_ORDER_STATUS = order.OS_ORDER_STATUS
    order_model.OP_ORDER_ID = order.OP_ORDER_ID
    order_model.OP_PROD_NAME = order.OP_PROD_NAME
    order_model.OP_PROD_ID = order.OP_PROD_ID
    order_model.OP_PROD_PRICE = order.OP_PROD_PRICE

    db.add(order_model)
    db.commit()
    return order


@app.put("/{book_id}")
def update_order(order_id: str, order: Order, db: Session = Depends(get_db)):
    order_model = db.query(models.Orders).filter(
        models.Orders.id == order_id).first()

    if order_model is None:
        raise HTTPException(
            status_code=404,
            detail=f"ID {order_id} : Does not exist"
        )

    order_model.OS_ORDER_CD = order.OS_ORDER_CD
    order_model.OS_CUST_NAME = order.OS_CUST_NAME
    order_model.OS_CUST_EMAIL = order.OS_CUST_EMAIL
    order_model.OS_CUST_PHONE_NUMBER = order.OS_CUST_PHONE_NUMBER
    order_model.OS_TOTAL_PRICE = order.OS_ORDER_CD
    order_model.OS_ORDER_STATUS = order.OS_ORDER_STATUS
    order_model.OP_ORDER_ID = order.OP_ORDER_ID
    order_model.OP_PROD_NAME = order.OP_PROD_NAME
    order_model.OP_PROD_ID = order.OP_PROD_ID
    order_model.OP_PROD_PRICE = order.OP_PROD_PRICE

    db.add(order_model)
    db.commit()
    return order


@app.delete("/{order_id}")
def delete_order(order_id: str, db: Session = Depends(get_db)):

    order_model = db.query(models.Orders).filter(
        models.Orders.OP_ORDER_ID == order_id).first()

    if order_model is None:
        raise HTTPException(
            status_code=404,
            detail=f"ID {order_id} : Does not exist"
        )

    db.query(models.Orders).filter(
        models.Orders.OP_ORDER_ID == order_id).delete()
    db.commit()
    return f"Order {order_id} deleted."
