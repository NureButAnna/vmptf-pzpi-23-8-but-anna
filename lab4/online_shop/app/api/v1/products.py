from fastapi import APIRouter, Depends, status

from app.models import User
from app.schemas.product import ProductCreate, ProductRead, ProductUpdate
from app.services.products import ProductService
from app.dependency import get_product_service, get_current_user, require_role

router = APIRouter(
    prefix="/products",
    tags=["Product🏷️"]
)

@router.get("/", response_model=list[ProductRead])
def get_products(service: ProductService = Depends(get_product_service),):
    return service.get_all_products()


@router.get("/{product_id}", response_model=ProductRead)
def get_product(
    product_id: int,
    service: ProductService = Depends(get_product_service)
):
    return service.get_product_by_id(product_id)


@router.post("/", response_model=ProductRead, status_code=status.HTTP_201_CREATED)
def create_product(
    product_data: ProductCreate,
    service: ProductService = Depends(get_product_service),
    current_user: User = Depends(require_role("адмін", "менеджер"))
):
    return service.create_product(product_data)


@router.put("/{product_id}", response_model=ProductRead, )
def update_product(
    product_id: int,
    product_data: ProductUpdate,
    service: ProductService = Depends(get_product_service),
    current_user: User = Depends(require_role("адмін", "менеджер"))
):
    return service.update_product(product_id, product_data)


@router.delete("/{product_id}", status_code=status.HTTP_200_OK)
def delete_product(
    product_id: int,
    service: ProductService = Depends(get_product_service),
    current_user: User = Depends(require_role("адмін", "менеджер"))
):
    return service.delete_product(product_id)