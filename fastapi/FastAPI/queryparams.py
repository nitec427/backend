from fastapi import FastAPI

app = FastAPI()
# Parameters except path parameters are interpreted as query params

fake_items = [{"item1": "foo"}, {"item2": "boo"}, {"item3": "zoo"}]

# Normally like all path components, query params are also string type. However, with python type hints they are converted to given types and validated.


@app.get("/items/")
async def main(skip: int = 0, limit: int = 10):
    return fake_items[skip: skip + limit]


@app.get("/items/")
async def get_items(skip: int = 0, limit: int = 10):
    return fake_items[skip: skip + limit]
