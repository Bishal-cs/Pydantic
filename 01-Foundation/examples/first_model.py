from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    is_active: bool

# here we have to give same name or key as in the class 
input_data = {
    "id": 1,
    "name": "Bishal Das",
    "is_active": True
}

user = User(**input_data)
print(user)