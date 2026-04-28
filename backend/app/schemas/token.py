from pydantic import BaseModel
from typing import Optional

class token(BaseModel):
    access_token : str 
    type_token : str 


    