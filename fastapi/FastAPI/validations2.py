# Here path parameters's and numerical validations are done

from fastapi import FastAPI, Query, Path
# Importing path, enables us to check given paths
app = FastAPI()


# @app.get("/items/{item_id}")
# async def read_items(
#     # Metadata can be given to path validations as well
#     # Part is always required so do use ... always
#     # Even if you put None or default value, Path still is required and forced by fastapi.
#     item_id: int = Path(...), title="The id of the item to get",
#     q: str | None = Query(None, alias="item-query")
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results


# @app.get("/items/{item_id}")
# async def read_items(
#     # Because Python will complain, if parameters do not come first, the order could be changed easily
#     q: str,
#     item_id: int = Path(...), title="The id of the item to get",
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results


@app.get("/items/{item_id}")
async def read_items(
    # * -> means that following parameters will be keyword arguments(kwargs), so q can come after item_id
    *,
    item_id: int = Path(..., title="The id of the item to get", ge=1), q: str
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
