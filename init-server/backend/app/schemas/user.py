import datetime
from pydantic import BaseModel, ConfigDict

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    pass

class UserOut(UserBase):
    id: int
    email: str
    created_at: datetime.datetime
    model_config = ConfigDict(from_attributes=True)
