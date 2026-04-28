from pydantic import BaseModel , ConfigDict
from typing import Optional
from app.models.route import RouteStatus
from datetime import datetime

class RouteCreate(BaseModel):
    agent_id : Optional[int] = None 
    admin_id : int 

class RouteUpdate(BaseModel):
    agent_id: Optional[int] = None
    status: Optional[RouteStatus] = None
    generated_at: Optional[datetime] = None 

class RouteResponse(BaseModel):
    id: int
    admin_id : int
    agent_id: Optional[int] = None
    status: RouteStatus
    generated_at: datetime
    model_config = ConfigDict(from_attributes=True)
