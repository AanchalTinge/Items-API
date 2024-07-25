# FastAPI Items API

## Overview

This project is a RESTful API built using [FastAPI](https://fastapi.tiangolo.com/) and [SQLite](https://www.sqlite.org/index.html). The API allows users to manage a collection of items with functionalities for CRUD (Create, Read, Update, Delete) operations and advanced search capabilities.

## Features

- **Create**: Add new items to the database.
- **Read**: Retrieve all items or specific items by ID.
- **Update**: Modify existing items.
- **Delete**: Remove items from the database.
- **Search**: Filter items based on name, description, price range, and quantity.

## Project Structure

```
fastapi_items/
├── database.py        # Contains database setup and initialization
├── crud.py            # Contains CRUD operations
├── main.py            # Main application file
├── models.py          # Database models
├── __init__.py        # Package initialization
├── venv/              # Virtual environment directory (if created)
└── items.db           # SQLite database file (will be created automatically)
```

## Installation

### Prerequisites

- Python 3.7 or higher
- `pip` (Python package installer)

### Steps to Set Up

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/fastapi_items.git
   cd fastapi_items
   ```

2. **Create and Activate a Virtual Environment** (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:

   ```bash
   pip install fastapi uvicorn sqlalchemy
   ```

4. **Initialize the Database**:

   The database will be automatically created when you run the application for the first time.

## Running the Application

1. **Start the FastAPI Application**:

   ```bash
   uvicorn main:app --reload
   ```

2. **Access the API Documentation**:

   Open your browser and navigate to `http://127.0.0.1:8000/docs` to interact with the API using the auto-generated Swagger UI.

## API Endpoints

- `POST /items/`: Create a new item.
- `GET /items/`: Retrieve all items.
- `GET /items/{item_id}`: Retrieve an item by ID.
- `PUT /items/{item_id}`: Update an item by ID.
- `DELETE /items/{item_id}`: Delete an item by ID.
- `GET /items/search/`: Search for items based on name, description, price range, and quantity.

## Example `curl` Commands

- **Create a new item**:

   ```bash
   curl -X 'POST' \
     'http://127.0.0.1:8000/items/' \
     -H 'accept: application/json' \
     -H 'Content-Type: application/json' \
     -d '{
     "name": "Item1",
     "description": "This is item 1",
     "price": 10.0,
     "quantity": 5
   }'
   ```

- **Retrieve all items**:

   ```bash
   curl -X 'GET' 'http://127.0.0.1:8000/items/' -H 'accept: application/json'
   ```

- **Retrieve an item by ID**:

   ```bash
   curl -X 'GET' 'http://127.0.0.1:8000/items/1' -H 'accept: application/json'
   ```

- **Update an item by ID**:

   ```bash
   curl -X 'PUT' \
     'http://127.0.0.1:8000/items/1' \
     -H 'accept: application/json' \
     -H 'Content-Type: application/json' \
     -d '{
     "name": "Updated Item",
     "description": "This is the updated item",
     "price": 15.0,
     "quantity": 10
   }'
   ```

- **Delete an item by ID**:

   ```bash
   curl -X 'DELETE' 'http://127.0.0.1:8000/items/1' -H 'accept: application/json'
   ```

- **Search for items**:

   ```bash
   curl -X 'GET' 'http://127.0.0.1:8000/items/search/?name=Item&price_min=5&price_max=15' -H 'accept: application/json'
   ```
