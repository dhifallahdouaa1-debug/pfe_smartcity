from sqlalchemy import Column,Integer,String,Boolean,DateTime,Enum
from app.core.database import Base 
import enum
from sqlalchemy.sql import func
class UserRole(str, enum.Enum):
    admin   = "admin"
    agent   = "agent"
    citizen = "citizen"
class User(Base):
    __tablename__="users"
    
    id=Column(Integer,primary_key=True,index=True)
    
    full_name=Column(String(100),nullable=False)
    
    email=Column(String(100),index=True,unique=True,nullable=False)
    
    hashed_password=Column(String(255),nullable=False)
    
    role=Column(Enum(UserRole),nullable=False,default=UserRole.citizen)
    
    is_active=Column(Boolean,default=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
