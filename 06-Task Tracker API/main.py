from schemas import Task, User_Read, User_Create, Create_Task
from memory import USERS, TASKS
from fastapi import FastAPI, HTTPException

user_id=1
task_id=1

app=FastAPI(
    title="Task Tracker API",
    description="This app will handle task tracking"
)


#root endpoint
@app.get("/")
def get_root():
    return {"message":"Task Tracking App is running..."}

# Users
# POST /users/ – create a user (return UserRead).
@app.post("/users/",response_model=User_Read)
def create_user(user:User_Create):
    global user_id
    new_user=User_Read(id=user_id, **user.model_dump())
    USERS[user_id]=new_user
    user_id+=1
    return new_user
    
# GET /users/{user_id} – retrieve user.
@app.get("/users/{user_id}")
def get_users(user_id:int):
    user=USERS.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail=f"User id {user_id} not found")
    return user

# Tasks
# POST/user/{user_id}/tasks – create a task (return full Task model).
@app.post("/user/{user_id}/tasks",response_model=Task)
def create_task(user_id:int, task:Create_Task):
    if user_id not in USERS:
        raise HTTPException(status_code=404,detail=f"User id {user_id} not found in Memory")
    
    global task_id
    new_task=Task(task_id=task_id,user_id=user_id, **task.model_dump())
    TASKS[user_id]=new_task
    task_id+=1
    return new_task

# GET /tasks/{task_id} – get task.
@app.get("/tasks/{task_id}")
def get_tasks(task_id:int):
    task=TASKS.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail=f"User id {user_id} not found")
    return task

# PUT /tasks/{task_id} – update status only, validating allowed values. 
@app.put("/tasks/{task_id}")
def update_status(task_id:int,status:str):
    if status not in {"Pending", "Completed", "In Progress"}:
        raise HTTPException(status_code=400, detail=f"'{status}' is not valid Status")
    task =TASKS.get(task_id)
    if not task:
        raise HTTPException(status_code=404,detail=f"Task with user id {user_id} not found")
    task.status=status
    return task

# GET /users/{user_id}/tasks – list all tasks for a user.
@app.get("/users/{user_id}/tasks")
def get_user_tasks(user_id:int):
    return [task for task in TASKS.values() if user_id == task.user_id]
