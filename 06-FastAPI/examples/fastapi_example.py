from fastapi import FastAPI, Depends
from pydantic import BaseModel, EmailStr

app = FastAPI()

class User(BaseModel):
    username: str
    email: EmailStr
    password: str

class Settings(BaseModel):
    app_name: str = "Test App"
    admin_email: str = "admin@test.com"

def get_settings():
    return Settings()

@app.post('/signup')
def signup(user: User):
    return {'message': f'User {user.username} Signup Successfully'}

@app.get('/settings')
def get_settings_endpoint(settings: Settings = Depends(get_settings)):
    return settings
    
