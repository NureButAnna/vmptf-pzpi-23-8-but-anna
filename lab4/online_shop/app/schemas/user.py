from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, EmailStr, field_validator, Field, ConfigDict

class UserBase(BaseModel):
    name: str
    surname: str
    email: EmailStr
    phone_number: Optional[str] = Field(None, max_length=15)

    model_config = ConfigDict(from_attributes=True)

class UserRegister(UserBase):
    password: str = Field(min_length=4)

class UserInDB(UserBase):
    password_hash: str
    created_at: datetime
    role: str

class UserRead(UserBase):
    id: int
    created_at: datetime
    role: str

class UserUpdate(BaseModel):
    name: Optional[str] = None
    surname: Optional[str] = None
    email: Optional[EmailStr] = None
    phone_number: Optional[str] = Field(None, max_length=15)
    password_hash: Optional[str] = Field(None, min_length=4)

    model_config = ConfigDict(from_attributes=True)

class UserRole(str, Enum):
    USER = "user"
    ADMIN = "admin"