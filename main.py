from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from enum import Enum

app = FastAPI()

items = []

@app.get("/")
async def root():
    return {"hey":"guys"}

# Endpoint to create items by using an http POST

@app.post("/items")
def create_item(item: str):
    items.append(item)
    return items

# List items endpoint

@app.get("/items")
def list_items(limit: int = 10):
    return items[0:limit]


# Endpoint for getting items by using an http GET with an if for item_id if not found

@app.get("/items/{item_id}")
def get_item(item_id: int) -> str:
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail="item not found in list")
