from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Person(BaseModel):
    id: int
    name: str
    origin: str

Users: List[Person] = []

@app.get('/')
def read_root():
    return {'Hello': 'World'}

@app.get('/users')
def read_users():
    return Users

@app.post('/users')
def add_user(user: Person):
    Users.append(user)
    return user

@app.put('/users/{user_id}')
def update_user(user_id: int, updated_user: Person):
    for index, user in enumerate(Users):
        if user.id == user_id:
            Users[index] = updated_user
            return updated_user
        
    return {'error': 'User not found'}

@app.delete('/users/{user_id}')
def delete_user(user_id: int):
    for index, user in enumerate(Users):
        if user.id == user_id:
            deleted_user = Users.pop(index)
            return deleted_user
        
    return {'error': 'User not found'}