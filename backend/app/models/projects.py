from sqlalchemy import Column, Integer, String, Text, Float, DateTime, Foreikey # type: ignore
from sqlalchemy.orm import relationship # type: ignore
from datetime import datetime
from ..database import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key = True, index = True)
    name = Column(String, nullable= False, index = True)
    description = Column(Text, nullable = False)
    category_id = Column(Integer, Foreikey("categories.id"), nullable = False)
    created_at = Column(DateTime, default= datetime.timezone.utc)
    school_obj = Column(String,nullable = False)

    category = relationship("Category", back_populates = "projects")

    def __repr__(self):
        return f"<Product(id={self.id}, name='{self.name}', school_obj='{self.school_obj}')"