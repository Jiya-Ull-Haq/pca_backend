from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    username: str
    password: str


class User(UserBase):
    id: int
    username: str

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    email: str
    password: str


class TaskBase(BaseModel):
    task: str
    assignee_id: int
    priority: Optional[str]
    due_date: Optional[datetime]


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    id: int
    creator_id: int
    status: str

    class Config:
        orm_mode = True


class TaskStatusUpdate(BaseModel):
    status: str
