from pydantic import BaseModel,Field
from datetime import datetime
from typing import Optional

class TodoBase(BaseModel):
    title:str

class TodoCreate(TodoBase):
    description:Optional[str] = ''

class TodoResponse(BaseModel):
    id:int
    user_id:int
    title:str
    description:str
    is_completed:bool = Field(default=False)
    created_at: datetime
    update_at: datetime

    class Config:
        orm_mode = True