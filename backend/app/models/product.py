from sqlalchemy import Column, Integer, String, Text, Float, DateTime, Foreikey # type: ignore
from sqlalchemy.orm import relationship # type: ignore
from datetime import datetime
from ..database import Base

class Product(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key = True, index = True)

    name = Column(String, nullable= False, index = True)

    description = Column(Text, nullable = False)

    price = Column(Float, nullable = False)

    category_id = Column(Integer, Foreikey("categories.id"), nullable = False)

    image_url = Column(String) 

    created_at = Column(DateTime, default= datetime.timezone.utc)


    category = relationship("Category", back_populates = "projects")

    def __repr__(self):
        return f"<Product(id={self.id}, name='{self.name}', price='{self.price}')"