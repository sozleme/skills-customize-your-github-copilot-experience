# Starter Code for Building REST APIs with FastAPI

# TODO: Install FastAPI and Uvicorn if not already installed
# pip install fastapi uvicorn

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

# TODO: Create FastAPI app instance
# app = FastAPI()

# TODO: Define Pydantic models for data validation
# class Item(BaseModel):
#     id: int
#     name: str
#     description: Optional[str] = None

# TODO: Initialize a list to store items
# items = []

# TODO: Define root endpoint
# @app.get("/")
# def read_root():
#     return {"message": "Welcome to FastAPI"}

# TODO: Define CRUD endpoints
# @app.get("/items")
# def read_items():
#     pass

# @app.post("/items")
# def create_item(item: Item):
#     pass

# @app.get("/items/{item_id}")
# def read_item(item_id: int):
#     pass

# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     pass

# @app.delete("/items/{item_id}")
# def delete_item(item_id: int):
#     pass

# TODO: Run the server with: uvicorn main:app --reload