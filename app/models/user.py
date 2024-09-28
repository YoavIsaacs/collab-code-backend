from typing import Optional
from datetime import datetime
from pydantic import EmailStr, BaseModel


class UserModel(BaseModel):
    id: Optional[str]
    username: str
    email: EmailStr
    hashed_password: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
