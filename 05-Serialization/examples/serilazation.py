from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class user(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    address: Address
    tags: List[str] = []
    createdAt: datetime
    model_config = ConfigDict(
        json_encoders = {
            datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S')}
    )

person = user(
    id=1,
    name="Bishal Das",
    email="bishal123@gmail.com",
    address = Address(
        street="Birendra Nagar",
        city="Chuchurah",
        zip_code="712102"
    ),
    tags=["Premium", "Best devoloper"],
    createdAt=datetime(2025,  6, 6, 3, 5, 42)
)

# main Serilazation part Using model_dump() -> dict

python_dict = person.model_dump()
print(python_dict)
print("___________________________________________________________________________________________________________________________\n")
# Using model_dump_json()
json_str = person.model_dump_json()
print(json_str)