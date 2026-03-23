from fastapi import FastAPI

app = FastAPI()

items = []

@app.get("/")
def root():
    return {"hey":"guys"}

# Endpoint to create items by using an http POST

@app.post("/items")
def create_item(item: str):
    items.append(item)
    return items

@app.get("/items/{item_id}")
def get_item(item_id: int) -> str:
    item = items[item_id]
    return item
