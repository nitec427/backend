from fastapi import FastAPI, Path, Body
from pydantic import BaseModel

app = FastAPI()
# Send your data with request body as JSON


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class User(BaseModel):
    name: str
    password: str


# @app.put("/items/{item_id}")
# async def update_item(
#     *,
#     item_id: int = Path(..., title="The ID of the item to get", ge=0, le=1000),
#     q: str | None = None,
#     item: Item | None = None,
#     user: User | None = None,
#     # Also singular variables can be forced to be input from request body
#     importance: int = Body(...)
# ):
#     print(importance)
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     if item:
#         results.update({"item": item})
#     if user:
#         results.update({"user": user})
#     return results

@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int = Path(..., title="The ID of the item to get", ge=0, le=1000),
    q: str | None = None,
    # Send item with its key
    item: Item = Body(..., embed=True),
    user: User | None = None,
    # Also singular variables can be forced to be input from request body
    # importance: int = Body(...)
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    if user:
        results.update({"user": user})
    return results
