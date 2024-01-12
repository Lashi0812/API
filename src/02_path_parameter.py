from fastapi import FastAPI
from enum import Enum

class Model(str,Enum):
    llama = "llama"
    gpt = "gpt"
    bert = "bert"

app = FastAPI()

@app.get("/path_parameter/{item_id}")
async def read_item(item_id):
    return {"message":item_id}


@app.get("/path_parameter_type/{item_id}")
async def read_item(item_id:int):
    return {"message":item_id}

@app.get("/pre_defined/{model_name}")
async def get_model(model_name:Model):
    return {"message":model_name}

@app.get("/files/{file_path:path}")
async def read_file(file_path):
    msg = []
    with open(file_path,"r") as f:
        msg = f.readlines()
    return {"message":msg}