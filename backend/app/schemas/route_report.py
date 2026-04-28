from pydantic import BaseModel , ConfigDict
from datetime import datetime 
from typing import Optional 
from app.models.route_report import StopStatus

class RouteReportCreate(BaseModel):
    route_id : int 
    report_id : int
    visit_order : int

class RouteReportUpdate(BaseModel):
    visit_order: Optional[int] = None
    status: Optional[StopStatus] = None
    
class RouteReportResponse(BaseModel):
    id: int
    route_id: int
    report_id: int
    visit_order: int
    visited_at: Optional[datetime] = None
    status: Optional[StopStatus] = None  

    model_config = ConfigDict(from_attributes=True)