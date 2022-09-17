from fastapi import FastAPI, Query

app = FastAPI()

# Whenever q is provided, limit its size to max 60.

# You can also force your query string to match the given regular expression pattern.


# @app.get("/")
# async def read_items(q: str | None = Query(None, max_length=60, min_length=20)):
#     results = {"items": [{"item_id": "Foo"}, {"item_id ": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# In case parameter must be required, then use ...(ellipsis) to force that parameter
# @app.get("/")
# async def read_items(q: str | None = Query(..., max_length=60, min_length=20)):
#     results = {"items": [{"item_id": "Foo"}, {"item_id ": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# We can also receive multiple values with Query


@app.get("/")
async def read_items(q: list[str] | None = Query(None)):
    results = {"items": [{"item_id": "Foo"}, {"item_id ": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# We can also provide a list of values


# @app.get("/items")
# async def read_items(q: list[str] = Query(["foo", "bar"])):
#     query_items = {"q": q}
#     return query_items

# Metadata can be provided for OpenAPI generation, and used by the documentation user interfaces
@app.get("/items")
async def read_items(q: list[str] = Query(None, title="Optional parameter", description="Wonderful voice")):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
