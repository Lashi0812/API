from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name:str
    desc:str|None = None
    count:int

@app.post("/")
async def create_item(item:Item):
    item_dict = item.model_dump()
    item_dict.update({"message":"got the message"})
    return item_dict

