from decimal import Decimal
from typing import Optional

from sqlalchemy import Numeric, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base

class OrderItems(Base):
    __tablename__ = "orderitems"
    id: Mapped[int] = mapped_column("order_item_id", primary_key=True, index=True)
    order_id: Mapped[int] = mapped_column(
        ForeignKey("orders.order_id", ondelete="CASCADE"),
        nullable=False
    )

    product_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("products.product_id", ondelete="SET NULL"),
        nullable=True
    )

    quantity: Mapped[int] = mapped_column(Integer, nullable=False, default=1)
    price_at_purchase: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False
    )

    order = relationship("Order", back_populates="order_items")

    product = relationship("Product")