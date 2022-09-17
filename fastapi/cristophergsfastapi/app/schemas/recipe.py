from pydantic import BaseModel, HttpUrl
from typing import Sequence
class RecipeBase(BaseModel):
    label: str
    source: str
    url: HttpUrl
    
class RecipeSearchResults(BaseModel):
    results: Sequence[Recipe]
    
class RecipeCreate(RecipeBase):
    label: str
    source: str
    url: HttpUrl
    submitter_id: int
    
class RecipeUpdate(RecipeBase):
    label:str
    
# Properties shared by models stored in Database

class RecipeInDBBase(RecipeBase):
    id: int
    submitter_id: int
    
    class Config:
        orm_mode = True
        
# Properties to return to client
class Recipe(RecipeInDBBase):
    pass

class RecipeInDB(RecipeInDBBase):
    pass