from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional
from datetime import datetime
from app.models.user import UserRole 

class UserCreate(BaseModel):
    full_name: str  
    email: EmailStr
    password: str 
    role: UserRole = UserRole.citizen #par defaut 

class UserUpdate(BaseModel):
    full_name: Optional[str]= None
    email: Optional[EmailStr]= None
    password: Optional[str]= None

class UpdatePassword(BaseModel):
    current_password : str
    new_password : str 

class UserLogin(BaseModel):
    email: EmailStr
    password : str

class UserResponse(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    role: UserRole
    is_active: bool
    created_at: datetime 
    model_config = ConfigDict(from_attributes=True)

     