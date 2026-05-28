from decimal import Decimal

from pydantic import BaseModel, ConfigDict
from app.schemas.product import ProductShort

class OrderItemRead(BaseModel):
    id: int
    product_id: int
    quantity: int
    price_at_purchase: Decimal
    product: ProductShort

    model_config = ConfigDict(from_attributes=True)

class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int
    price_at_purchase: Decimal
