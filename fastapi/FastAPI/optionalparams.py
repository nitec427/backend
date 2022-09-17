from fastapi import FastAPI
from typing import Optional
app = FastAPI()
# Parameters except path parameters are interpreted as query params

fake_items = [{"item1": "foo"}, {"item2": "boo"}, {"item3": "zoo"}]

# Normally like all path components, query params are also string type. However, with python type hints they are converted to given types and validated.


# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: Optional[str] = None, short: bool = False):
#     item = {"item_id":item_id}
#     if q:
#         return {"item_id": item_id, "q": q}
#     else:
#         return {"item_id": item_id}
# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: Optional[str] = None, short: bool = False):
#     item = {"item_id": item_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update({"description": "Amazing object to possess"})
#     return item

# Multiple path and query parameters can be given to the model as you wish

@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: Optional[str] = None, short: bool = False
):
    item = {"item_id": item_id, "user_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"desc": "Hello Mom"})
    return item
