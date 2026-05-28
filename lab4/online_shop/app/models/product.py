from decimal import Decimal
from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, Text, Numeric, Integer

from app.database import Base

class Product(Base):
    __tablename__ = "products"
    id: Mapped[int] = mapped_column("product_id", primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(150))
    producer: Mapped[Optional[str]] = mapped_column(String(100))
    description:  Mapped[Optional[str]] = mapped_column(Text)
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    stock: Mapped[int] = mapped_column(Integer)

    category_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("categories.category_id", ondelete="SET NULL"),
        nullable=True
    )

    category = relationship("Category", back_populates="products")
    reviews = relationship("Review", back_populates="product")