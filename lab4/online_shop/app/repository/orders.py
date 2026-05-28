from sqlalchemy.orm import selectinload

from ..models.order import Order
from ..models.order_items import OrderItems
from ..repository.base import BaseRepository


class OrderRepository(BaseRepository):
    model = Order

    def get_by_user_id(self, user_id: int):
        return (
            self.db.query(Order)
            .filter(Order.user_id == user_id)
            .options(
                selectinload(Order.order_items)
                .selectinload(OrderItems.product),
                selectinload(Order.user)
            )
            .all()
        )

    def get_by_product_id(self, product_id: int):
        return (
            self.db.query(Order)
            .filter(Order.product_id == product_id)
            .options(
                selectinload(Order.order_items)
                .selectinload(OrderItems.product),
                selectinload(Order.user)
            )
            .all()
        )