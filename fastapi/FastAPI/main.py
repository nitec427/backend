from fastapi import FastAPI
from enum import Enum
app = FastAPI()

# Tutorial - User Guide introuction


# FastAPI generates a "schema" with all our API
# using openAPI standard


# Definition or description of sth (schema). Not the code that implements it.

# We can also use possible parameter path values predefined with inhering both from the base class and Enum
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get('/')
async def root():
    return {"message": "Hello, world!"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
# Path parameters


@app.get("/users/me")
def get_me():
    return {"user": "Celal Şengör"}


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user": user_id}


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    print(model_name)
    if model_name == ModelName.alexnet:
        return {"Model name": model_name, "message": "Deep learning is splendid "}
    elif model_name == ModelName.resnet:
        return {"Model name": model_name, "message": "Resnet is thorough "}
    elif model_name.value == "lenet":
        return {"Model name": model_name, "message": "Lenet is reached through enum value "}

# Path as parameters. Normally in OpenAPI, there is no method to put path to your routes. However, in FastAPI this is possible.

# If you do not provide that the below route accepts path as parameter then you get an object as a response which indicates that route is not found


@app.get("/files/{file_path}")
async def read_file(file_path: str):
    return {"file_path": file_path}
