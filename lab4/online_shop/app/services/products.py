from typing import List

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.product import ProductCreate, ProductRead, ProductUpdate
from app.repository.products import ProductRepository


class ProductService:
    def __init__(self, db: Session):
        self.repository = ProductRepository(db)

    def get_all_products(self) -> List[ProductRead]:
        products = self.repository.get_all()
        return [ProductRead.model_validate(p) for p in products]

    def get_product_by_id(self, product_id: int) -> ProductRead:
        product = self.repository.get_by_id(product_id)

        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Product with id {product_id} not found"
            )

        return ProductRead.model_validate(product)

    def create_product(self, data: ProductCreate) -> ProductRead:
        product = self.repository.create(
            data.model_dump()
        )

        return ProductRead.model_validate(product)

    def update_product(self, product_id: int, data: ProductUpdate) -> ProductRead:
        updated = self.repository.update(
            product_id,
            data.model_dump(exclude_unset=True)
        )

        if not updated:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Product with id {product_id} not found"
            )

        return ProductRead.model_validate(updated)

    def delete_product(self, product_id: int):
        deleted = self.repository.delete(product_id)

        if not deleted:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Product with id {product_id} not found"
            )

        return {"message": "Product deleted successfully"}