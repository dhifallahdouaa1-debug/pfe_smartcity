from pydantic import BaseModel , ConfigDict
from typing import Optional
from datetime import datetime
from app.models.report import ReportStatus # in report we can add category of report too in models nd here

class CreatReport(BaseModel):
    longitude : float
    latitude : float
    audio_path : Optional[str] = None
    ##image_path we can add it maybe? 
    address_text : Optional[str] = None 

class ReportUpdate(BaseModel):
    status : Optional[ReportStatus] = None

class ReportResponse(BaseModel):
    id : int 
    citizen_id : int
    longitude : float
    latitude : float
    audio_path : Optional[str] = None
    address_text : Optional[str] = None 
    status : ReportStatus 
    created_at : datetime 

    model_config= ConfigDict(from_attributes=True)



    