from pydantic import BaseModel
from typing import List, Dict, Optional

class Cart(BaseModel):
    user_id: int
    items: list[str]
    quantity: dict[str, int]

class BlogPost(BaseModel):
    title: str
    content: str
    img_url: Optional[str] = None # Optional field with default value

