from typing import List

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.order import OrderCreate, OrderRead, OrderUpdate
from ..models import Order, Product
from ..models.order_items import OrderItems

from ..repository.orders import OrderRepository


class OrderService:
    def __init__(self, db: Session):
        self.repository = OrderRepository(db)

    def get_all_orders(self) -> List[OrderRead]:
        orders = self.repository.get_all()
        return [OrderRead.model_validate(o) for o in orders]

    def get_order_by_id(self, order_id: int) -> OrderRead:
        order = self.repository.get_by_id(order_id)

        if not order:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Order with id {order_id} not found"
            )

        return OrderRead.model_validate(order)

    def get_orders_by_user(self, user_id: int) -> List[OrderRead]:
        orders = self.repository.get_by_user_id(user_id)
        return [OrderRead.model_validate(o) for o in orders]

    def create_order(self, data: OrderCreate) -> OrderRead:
        total_price = 0

        new_order = Order(
            user_id=data.user_id,
            status=data.status,
            total_price=0
        )

        self.repository.db.add(new_order)
        self.repository.db.flush()

        for item in data.order_items:
            product = self.repository.db.query(Product).filter(
                Product.id == item.product_id
            ).first()

            if not product:
                raise ValueError("Product not found")

            price = product.price
            subtotal = price * item.quantity
            total_price += subtotal

            order_item = OrderItems(
                order_id=new_order.id,
                product_id=item.product_id,
                quantity=item.quantity,
                price_at_purchase=price
            )

            self.repository.db.add(order_item)

        new_order.total_price = total_price

        self.repository.db.commit()
        self.repository.db.refresh(new_order)

        return new_order

    def update_order(self, order_id: int, data: OrderUpdate) -> OrderRead:
        updated = self.repository.update(
            order_id,
            data.model_dump(exclude_unset=True)
        )

        if not updated:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Order not found"
            )

        return OrderRead.model_validate(updated)

    def delete_order(self, order_id: int):
        deleted = self.repository.delete(order_id)

        if not deleted:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Order not found"
            )

        return {"message": "Order deleted successfully"}