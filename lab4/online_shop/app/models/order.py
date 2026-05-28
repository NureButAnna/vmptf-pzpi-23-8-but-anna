from decimal import Decimal
import datetime
from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, Numeric, text

from app.database import Base

class Order(Base):
    __tablename__ = "orders"
    id: Mapped[int] = mapped_column("order_id", primary_key=True, index=True)
    total_price: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    order_date:  Mapped[datetime.datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())")
    )
    status: Mapped[Optional[str]] = mapped_column(String(50), default="новий")

    user_id: Mapped[int] = mapped_column(ForeignKey(
        "users.user_id", ondelete="CASCADE"))

    user = relationship("User", back_populates="orders")

    order_items = relationship("OrderItems", back_populates="order",
        cascade="all, delete-orphan"
    )

