from fastapi import FastAPI 
from app.core.database import Base,engine
from app.models.user import User
from app.models.route import route 
from app.models.report import Report 
from app.models.route_report import RouteReport

app = FastAPI()

@app.get("/")
def root():
    return {"messg": "backend"}
#create tables 
Base.metadata.create_all(bind=engine) 