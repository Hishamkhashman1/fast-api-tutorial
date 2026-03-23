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
    return item
