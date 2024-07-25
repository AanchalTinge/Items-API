# main.py
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import init_db, SessionLocal
import crud

app = FastAPI()

# Initialize database
init_db()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Items API"}

# Existing endpoints
# ...

@app.post("/items/")
def create_item(name: str, description: str, price: float, quantity: int, db: Session = Depends(get_db)):
    return crud.create_item(db, name, description, price, quantity)

@app.get("/items/")
def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items

@app.get("/items/{item_id}")
def read_item(item_id: int, db: Session = Depends(get_db)):
    item = crud.get_item(db, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.put("/items/{item_id}")
def update_item(item_id: int, name: str, description: str, price: float, quantity: int, db: Session = Depends(get_db)):
    item = crud.update_item(db, item_id, name, description, price, quantity)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.delete("/items/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    item = crud.delete_item(db, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"detail": "Item deleted"}

@app.get("/items/search/")
def search_items(name: str = None, description: str = None, price_min: float = None, price_max: float = None, quantity: int = None, db: Session = Depends(get_db)):
    items = crud.search_items(db, name, description, price_min, price_max, quantity)
    return items
