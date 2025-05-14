from typing import List, Optional
from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    postal_code: str

class Person(BaseModel):
    id: int 
    name: str
    address: Address

class Comments(BaseModel):
    id: int
    content: str
    replies: Optional[list['Comments']] = None

Comments.model_rebuild()

address = Address(
    street= "Birendra Nagar",
    city= "Chinsurah",
    postal_code= "712102"
)

user = Person(
    id= 1,
    name= "Bishal Das",
    address= address
)
comments = Comments(
    id= 1,
    content= "1st Comments",
    replies= [
        Comments(id= 2, content= 'rply'),
        Comments(id= 3, content= 'rply2')
    ]
)