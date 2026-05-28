from datetime import datetime
from decimal import Decimal
from typing import Optional
from app.schemas.order_item import OrderItemRead, OrderItemCreate

from pydantic import BaseModel, EmailStr, field_validator, Field, ConfigDict

class OrderBase(BaseModel):
    total_price: Decimal
    order_date: datetime
    status: str
    user_id: int
    model_config = ConfigDict(from_attributes=True)

class OrderCreate(BaseModel):
    user_id: int
    status: str

    order_items: list[OrderItemCreate]

class OrderRead(BaseModel):
    id: int
    total_price: Decimal
    order_date: datetime
    status: str
    user_id: int

    order_items: list[OrderItemRead] = []

    model_config = ConfigDict(from_attributes=True)

class OrderUpdate(OrderBase):
    total_price: Optional[Decimal] = None
    status: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)
