from typing import Union
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

print(BaseModel)
class ItemType(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

# Get endpoint
@app.get("/")
def retrieve():
    return {"greeting":"hello from naimal"}

# Post endpoint
@app.post("/login")
def login(email:str,password:str):
    correct_pass="admin123"
    correct_email="naimalarain@gmail.com"
   
    if password==correct_pass and email==correct_email:
         return({"message":"login Successful"})
    else:
        raise HTTPException(
            status_code=401,
            detail="Please enter the correct password, Here are the hard-coded crendentials email:naimalarain@gmail.com, password:admin123"
        )
    
       
# Get endpoint with query parameter
@app.get("/items/{item_id}")
def path_query(item_id: int, q: Union[str,None] = None):
    return {"item_id": item_id, "q": q}


# Put endpoint
@app.put("/items/{item_id}")
def modify(item_id: int, item: ItemType):
    return {"item_name": item.name, "item_id": item_id, "item_price":item.price, "is_offer":item.is_offer}


