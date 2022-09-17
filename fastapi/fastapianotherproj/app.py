try:
    from fastapi import FastAPI
    from pydantic import BaseModel
    from bson.objectid import ObjectId
    from datetime import datetime
    import motor.motor_asyncio
except Exception as e:
    print("Error: ", e)
    
    
app = FastAPI()

MONGO_DETAILS = "mongodb+srv://nitec_427:70657065@cluster0.m7lhg6y.mongodb.net/test"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.FASTAPI

FASTAPI_collection = database.get_collection("FasterAPI")
def schema_helper(data) -> dict:
    '''
    helper to make the mongo query into dict form
    '''
    return {
        "id": str(data["_id"]),
        "SKU": data["sku"],
        "Brand Name": data["brand_name"],
        "Title": data["title"],
        "Thumbnail":  data["thumbnail"],
        "Available Price":  data["price"],
        "MRP":  data["mrp"]
    }


class Items(BaseModel):
    sku: str
    brand_name: str
    title: str
    thumbnail: str
    price: str
    mrp: str

@app.get("/")
async def get_all_data():
    datas = []
    async for data in FASTAPI_collection.find():
        datas.append(schema_helper(data))
    return datas

@app.get("/{data_id}")
async def get_data(data_id:str):
    data_data = await FASTAPI_collection.find_one({"_id": ObjectId(data_id)})
    return schema_helper(data_data)


@app.post('/new/')
async def post_data(item:dict ) -> dict:
    data_data = await FASTAPI_collection.insert_one(item)
    new_data = await FASTAPI_collection.find_one({"_id": ObjectId(data_data.inserted_id)})
    return schema_helper(new_data)

@app.delete('delete_data/{data_id}')
async def delete_data(data_id:str):
    data = await FASTAPI_collection.find_one({"_id": ObjectId(data_id)})
    if data:
        await FASTAPI_collection.delete_one({"_id": ObjectId(data_id)})
        return True
    return False

@app.put('/update_data/{data_id}')
async def update_data(id: str, data:dict):
    if len(data) < 1:
        return False
    
    data = await FASTAPI_collection.find_one({"_id": ObjectId(id)})
    data.update({"update":True, "updated_time":datetime.now()})
    if data:
        updated_data = await FASTAPI_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_data:
            return True
        return False