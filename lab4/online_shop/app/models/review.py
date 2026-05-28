from typing import Optional
import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, Text, Integer, text

from app.database import Base

class Review(Base):
    __tablename__ = "reviews"
    id: Mapped[int] = mapped_column("review_id", primary_key=True, index=True)
    rating: Mapped[int] = mapped_column(Integer)
    comment:  Mapped[Optional[str]] = mapped_column(Text)
    created_at: Mapped[datetime.datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())")
    )

    user_id: Mapped[Optional[int]] = mapped_column(ForeignKey(
        "users.user_id", ondelete="SET NULL"), nullable=True)

    product_id: Mapped[int] = mapped_column(ForeignKey(
        "products.product_id", ondelete="CASCADE"))

    user = relationship("User", back_populates="reviews")
    product = relationship("Product", back_populates="reviews")