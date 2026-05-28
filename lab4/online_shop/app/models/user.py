from datetime import datetime
from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text

from app.database import Base

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column("user_id", primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100))
    surname: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(unique=True,nullable=False)
    phone_number: Mapped[Optional[str]]= mapped_column(String(100))
    password_hash: Mapped[str] = mapped_column(Text,nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    role: Mapped[str] = mapped_column(String,nullable=False,default="користувач")

    orders = relationship("Order", back_populates="user")
    reviews = relationship("Review", back_populates="user")