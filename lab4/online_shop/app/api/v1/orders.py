from fastapi import APIRouter, Depends, status

from app.models import User
from app.schemas.order import OrderRead, OrderUpdate, OrderCreate
from app.services.orders import OrderService
from app.dependency import get_order_service, require_role

router = APIRouter(
    prefix="/orders",
    tags=["Order 📝"]
)

@router.get("/", response_model=list[OrderRead])
def get_orders(service: OrderService = Depends(get_order_service),
               current_user: User = Depends(require_role("адмін", "менеджер"))
               ):
    return service.get_all_orders()


@router.get("/{order_id}", response_model=OrderRead)
def get_order(order_id: int, service: OrderService = Depends(get_order_service),
                current_user: User = Depends(require_role("користувач", "адмін", "менеджер"))
              ):
    return service.get_order_by_id(order_id)


@router.get("/user/{user_id}", response_model=list[OrderRead])
def get_user_orders(
        user_id: int,
        service: OrderService = Depends(get_order_service),
        current_user: User = Depends(require_role("користувач"))
):
    return service.get_orders_by_user(user_id)


@router.put("/{order_id}", response_model=OrderRead)
def update_order(
    order_id: int,
    order_data: OrderUpdate,
    service: OrderService = Depends(get_order_service),
    current_user: User = Depends(require_role("адмін", "менеджер"))):
    return service.update_order(order_id, order_data)


@router.post("/",response_model=OrderCreate, status_code=status.HTTP_201_CREATED)
def add_order(order_data: OrderCreate, service: OrderService = Depends(get_order_service),
              current_user: User = Depends(require_role("клієнт", "адмін", "менеджер"))
              ):
    return service.create_order(order_data)


@router.delete("/",response_model=OrderRead, status_code=status.HTTP_200_OK)
def delete_order(order_id: int, service: OrderService = Depends(get_order_service),
                 current_user: User = Depends(require_role("адмін", "менеджер"))):
    return service.delete_order(order_id)