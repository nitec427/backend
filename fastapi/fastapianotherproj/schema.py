from pydantic import BaseModel

class Items(BaseModel):
    sku: str
    brand_name: str
    title: str
    thumbnail: str
    price: str
    mrp: str
    
def schema_helper(task) -> dict:
    """Helper function to make mongo query dict"""
    
    return {
        "id": str(task["_id"]),
        "SKU": task["sku"],
        "Brand Name": task["brand_name"],
        "Title": task["title"],
        "Thumbnail": task["thumbnail"],
        "Available Price": task["price"],
        "MRP": task["mrp"]
    }