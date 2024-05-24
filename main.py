from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
  name:str
  description:str
  price:float
  tax:float

app = FastAPI()

@app.post("/")
async def read_root(item:Item):
  return item