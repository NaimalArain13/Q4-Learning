from fastapi import FastAPI, Path, Query, Body
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    
app=FastAPI()

@app.get("/item/{item_id}")
async def get_user(
    item_id:int=Path(
        ...,
        title="The id of the item",
        description="any random id",
        ge=1
    )
):
  return {"item_id":item_id}
    
    
@app.get("/item/")
async def read_item(
    q:str|None=Query(
      None,
      title="query string",
      description="short query description",
      min_length=3,
      max_length=50
  ),
  skip:int=Query(0, ge=0),  # Greater than or equal to 0
  limit: int = Query(10, le=100)
):
    return {"q":q,"skip":skip,"limit":limit}


@app.put("/items/validated/{item_id}")
async def update_item(
    item_id: int = Path(..., title="Item ID", ge=1),
    q: str | None = Query(None, min_length=3),
    item: Item | None = Body(None, description="Optional item data (JSON body)")
):
    result = {"item_id": item_id}
    if q:
        result.update({"q": q})
    if item:
        result.update({"item": item.model_dump()})
    return result