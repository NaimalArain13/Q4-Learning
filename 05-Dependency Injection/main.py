from fastapi import FastAPI, Depends, Query, HTTPException
from typing import Annotated

# 1. Hello Dependency
def get_simple_goal():
    return {"message":"Here is my goal👀"}

app=FastAPI()

@app.get("/get-simple-goal")
def get_simple_goal(response:Annotated[dict,Depends(get_simple_goal)]):
    return response

# 2. Dependency with Parameter
def get_username(user:str):
    return {"This is username": user}

@app.get("/user")
def get_user(response:Annotated[dict,Depends(get_username)]):
    return response


# 3. Dependency with Query Parameters
def login_check(email:str=Query(None), password:str=Query(None)):
    if email and password=="1234":
        return {"message" : "Login Successful"}
    else:
        return {"message" : "Login Failed"}
        
@app.get("/login")
def check_login(user:Annotated[dict, Depends(login_check)]):
    return user


# 4. Multiple Dependencies
def numFunc1(num):
    num=int(num)
    num+=1
    return num

def numFunc2(num):
    num=int(num)
    num+=2
    return num

@app.get("/main/{num}")
def get_main(num:int,num1:Annotated[int, Depends(numFunc1)],num2:Annotated[int, Depends(numFunc2)]):
    total = num + num1 + num2
    return f"Pakistan {total}"


# 5. Class
blogs={
    "1":"blog 1",
    "2":"blog 2",
    "3":"blog 3" 
}

users={
    "5":"shurem",
    "6":"ali",
    "7":"rafay"
}

class getObjor404:
    def __init__(self, model):
        self.model=model
    def __call__(self, id:str):
        obj=self.model.get(id, None)
        if not obj:
            raise HTTPException(status_code=404, detail=f"Object ID {id} not found")
        return obj
blog_dependency=getObjor404(blogs)

@app.get("/blog/{id}")
def get_blog_obj(blog:Annotated[str, Depends(blog_dependency)]):
    return blog
user_dependency=getObjor404(users)

@app.get("/user/{id}")
def get_blog_obj(user:Annotated[str, Depends(user_dependency)]):
    return user