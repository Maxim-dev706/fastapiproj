from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from .category import CategoryResponse

class ProjectBase(BaseModel):
    name: str = Field(..., min_length= 1, max_length = 100,
                      description = "Project name")
    description : Optional[str] = Field(None, description ="Project description")
    school_obj : str = Field(..., min_length = 3, max_length = 20, description = "School object")

    category_id : int = Field(...,description = "Categoey ID")
    image_url : Optional[str] = Field(None, description = "Project image URL")

    class ProjectCreate(ProjectBase):
        pass

    class ProjectResponse(BaseModel):
        id : int = Field(..., decription = "Unique project ID")
        name :str
        description: Optional[str]
        school_obj: str
        category_id : int
        image_url: Optional[str]
        created_at: datetime
        category: CategoryResponse = Field(..., description = "Project category details")

        class Config:
            form_attributes = True

    class ProjectListResponse(BaseModel):
        projects: list[ProjectResponse]
        total: int = Field(..., description = "Total number of projects")

