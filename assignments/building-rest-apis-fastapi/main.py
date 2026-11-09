from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Items API")

items = [
    {"id": 1, "name": "Laptop", "description": "Portable computer"},
    {"id": 2, "name": "Mouse", "description": "Used for navigation"},
]


class Item(BaseModel):
    name: str
    description: str = ""


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI API"}


@app.get("/items")
def get_items():
    return items


@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")


@app.post("/items")
def create_item(item: Item):
    new_item = {
        "id": len(items) + 1,
        "name": item.name,
        "description": item.description,
    }
    items.append(new_item)
    return new_item


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    for index, existing_item in enumerate(items):
        if existing_item["id"] == item_id:
            updated_item = {
                "id": item_id,
                "name": item.name,
                "description": item.description,
            }
            items[index] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for index, item in enumerate(items):
        if item["id"] == item_id:
            del items[index]
            return {"message": f"Item {item_id} deleted"}
    raise HTTPException(status_code=404, detail="Item not found")
