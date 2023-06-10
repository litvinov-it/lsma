# Imports
# pydantic - типизирует
from pydantic import BaseModel
from datetime import datetime

# Init base schema for Post
class PostBase(BaseModel):
    title: str
    content: str

# Init standart schema for Post
class Post(PostBase):
    id: int
    created_at: datetime

    # Позволяет pydantic обрабатывать объекты sqlalchemy в JSON
    class Config:
        orm_mode = True

# Init cerate schema for Post
class PostCreate(PostBase):
    published: bool = True