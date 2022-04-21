from typing import List, Optional, Any

from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


class User(UserBase):
    id: int
    is_active: bool


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


class UserInDB(User):
    hashed_password: str
