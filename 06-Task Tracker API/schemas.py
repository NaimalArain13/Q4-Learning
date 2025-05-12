from pydantic import BaseModel, EmailStr, constr, field_validator
from datetime import date
UsernameStr = constr(min_length=3, max_length=20)

class User_Create(BaseModel):
    username: UsernameStr 
    email: EmailStr
    

class User_Read(User_Create):
    id:int
    
    
class Task(BaseModel):
    task_id:int
    title:str
    description:str
    status:str
    due_date:date
    user_id:int

    
class Create_Task(BaseModel):
    title:str
    description:str
    status:str
    due_date:date

    @field_validator('due_date')
    @classmethod
    def validate_due_date(cls, v:date):
        if v < date.today():
            raise ValueError("Due date must be today or a future date")
        return v