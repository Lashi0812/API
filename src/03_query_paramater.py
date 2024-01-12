from fastapi import FastAPI

app = FastAPI()

fake_db = [{"item": 1}, {"item": "23"}, {"item": 23}]


@app.get("/query")
async def read_db(s: int, e: int):
    return fake_db[s:e]


@app.get("/query_with_default")
async def read_db(s: int = 0, e: int = 3):
    return fake_db[s:e]


@app.get("/query_with_optional")
async def read_db(e: int | None = None, s: int = 0):
    return fake_db[s:e]
