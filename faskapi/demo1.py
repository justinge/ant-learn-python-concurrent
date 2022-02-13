from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "hello world"}


@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}


@app.get("/items1/{item_id}")
async def read_item(item_id: int):
    return {"item_id1": item_id}


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: int):
    return {"user_id": user_id}


from enum import Enum


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return "alexnet"
    elif model_name == ModelName.lenet:
        return "lenet"
    else:
        return "resnet"


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items3/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip:skip + limit]


from typing import Optional


@app.get("/items5/{item_id}")
async def read_item(item_id: str, q: Optional[str] = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


@app.get("/items6/{item_id}")
async def read_item(item_id: str, q: Optional[str] = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "This is an amazing item that has a long description"})

    return item


from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = 0.0001


@app.post("/items7/")
async def create_item(item: Item):
    return item


@app.get("/items8")
async def read_items(q: Optional[str] = Query(None, min_length=3, max_length=50)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "bar"}]}
    if q:
        results.update({"q": q})
    return results
