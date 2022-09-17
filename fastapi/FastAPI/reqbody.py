from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    # Pipes handle the jobs of Optional for previous examples
    tax: float | None = None


app = FastAPI()

# First we need to improt BaseModel from Pydantic


@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    item.name = "Plate"
    item.description = "Thing to eat on"
    item.price = 30
    item.tax = 5
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item

# path parameters
# pydantic based parameters (Item)
# query parameters


@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item, q: str | None = None):
    return {"item_id": item_id, **item.dict()}
