from pydantic import BaseModel

# TODO: Create a Pydantic model with id, name, price, in_stock

class Product(BaseModel):
    id : int
    name : str
    price : float
    in_stock : bool = True # This is a default value '= True'