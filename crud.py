# crud.py
from sqlalchemy.orm import Session
from models import Item

def create_item(db: Session, name: str, description: str, price: float, quantity: int):
    db_item = Item(name=name, description=description, price=price, quantity=quantity)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_items(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Item).offset(skip).limit(limit).all()

def get_item(db: Session, item_id: int):
    return db.query(Item).filter(Item.id == item_id).first()

def update_item(db: Session, item_id: int, name: str, description: str, price: float, quantity: int):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item:
        db_item.name = name
        db_item.description = description
        db_item.price = price
        db_item.quantity = quantity
        db.commit()
        db.refresh(db_item)
    return db_item

def delete_item(db: Session, item_id: int):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item

def search_items(db: Session, name: str = None, description: str = None, price_min: float = None, price_max: float = None, quantity: int = None):
    query = db.query(Item)
    if name:
        query = query.filter(Item.name.like(f"%{name}%"))
    if description:
        query = query.filter(Item.description.like(f"%{description}%"))
    if price_min is not None:
        query = query.filter(Item.price >= price_min)
    if price_max is not None:
        query = query.filter(Item.price <= price_max)
    if quantity is not None:
        query = query.filter(Item.quantity == quantity)
    return query.all()
