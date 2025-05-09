# Learned about pydantic BaseModel, ValidationError, nested models, EmailStr
from pydantic import BaseModel, ValidationError, EmailStr, field_validator

class Subject(BaseModel):
    sub_name:str
    sub_code:int
class User(BaseModel):
    id:int
    name:str
    email:EmailStr
    sub_detail:Subject
    @field_validator("name")
    def check_name(cls, v):
        if len(v)<2:
            raise ValueError("name should be atleast two characters long")
        return v
            
    
# test with valid data
data={"id":1,"name":"na","email":"naimalarain13@gmail.com", "sub_detail":{"sub_name":"English", "sub_code":21}}
user=User(**data)
user1=User.model_validate(user)
obj_user=user1.model_dump()
print(user)
print(obj_user)

# test with invalid data to see ValidationError in practical
try:
   invalidData={"id":"abcd","name":"n", "email":"naimalarain@gmail.com"}
   user2=User(**invalidData)
except ValidationError as e:
    print(e)



