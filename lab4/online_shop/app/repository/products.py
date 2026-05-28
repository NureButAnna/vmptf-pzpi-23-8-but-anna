from sqlalchemy.orm import selectinload

from ..models.product import Product
from ..repository.base import BaseRepository


class ProductRepository(BaseRepository):
    model = Product

    def get_by_category_id(self, category_id: int):
        return (
            self.db.query(Product)
            .options(
                selectinload(Product.category)
            )
            .filter(Product.category_id == category_id)
            .all()
        )