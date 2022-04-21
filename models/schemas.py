from typing import List, Optional, Any

from pydantic import BaseModel


class UserBase(BaseModel):
    
    class Config:
        orm_mode = True


class User(UserBase):
    id: int
    is_active: bool
    username: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


class UserInDB(User):
    hashed_password: str
