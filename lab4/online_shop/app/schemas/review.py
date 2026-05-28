from typing import Optional
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

class ReviewBase(BaseModel):
    user_id: Optional[int] = None
    product_id: int
    rating: int
    comment: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)

class ReviewCreate(ReviewBase):
    pass

class ReviewRead(ReviewBase):
    id: int

class ReviewUpdate(BaseModel):
    user_id: Optional[int] = None
    product_id: Optional[int] = None
    rating: Optional[int] = None
    comment: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)
