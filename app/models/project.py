from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel

class ProjectModel(BaseModel):
    id: Optional[str]
    name: str
    description: Optional[str]
    owner_id: str
    collaborator_ids: List[str] = []
    code: Optional[str] = str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
