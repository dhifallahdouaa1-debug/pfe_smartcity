from sqlalchemy import Column,Integer,String,Boolean, ForeignKey,Enum,DateTime
from app.core.database import Base 
import enum
from sqlalchemy.sql import func
class RouteStatus(str, enum.Enum):
    planned  = "planned"
    in_progress = "in_progress"
    completed = "completed"

class route(Base):
    __tablename__="routes"
    
    id=Column(Integer,primary_key=True,index=True)

    admin_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    agent_id = Column(Integer, ForeignKey("users.id"), nullable=True)

    status = Column(Enum(RouteStatus), nullable=False, default=RouteStatus.in_progress)

    generated_at = Column(DateTime(timezone=True), server_default=func.now())