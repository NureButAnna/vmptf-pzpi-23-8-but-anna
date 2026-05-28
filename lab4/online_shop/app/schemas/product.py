from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, EmailStr, field_validator, Field, ConfigDict

class ProductBase(BaseModel):
    name: str
    producer: Optional[str]
    description: str
    price: Decimal
    stock: int
    category_id: Optional[int]
    model_config = ConfigDict(from_attributes=True)

class ProductCreate(ProductBase):
    pass

class ProductRead(ProductBase):
    id: int

class ProductUpdate(ProductBase):
    name: Optional[str] = None
    producer: Optional[str] = None
    description: Optional[str] = None
    price: Optional[Decimal] = None
    stock: Optional[int] = None
    category_id: Optional[int] = None

    model_config = ConfigDict(from_attributes=True)

class ProductShort(BaseModel):
    id: int
    name: str
    price: Decimal

    model_config = ConfigDict(from_attributes=True)

