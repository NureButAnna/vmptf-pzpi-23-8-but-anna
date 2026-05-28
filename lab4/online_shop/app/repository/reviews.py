from sqlalchemy.orm import selectinload

from ..models.review import Review
from ..repository.base import BaseRepository


class ReviewRepository(BaseRepository):
    model = Review

    def get_by_product_id(self, product_id: int):
        return (
            self.db.query(Review)
            .options(
                selectinload(Review.user),
                selectinload(Review.product)
            )
            .filter(Review.product_id == product_id)
            .all()
        )

    def get_by_user_id(self, user_id: int):
        return (
            self.db.query(Review)
            .options(
                selectinload(Review.user),
                selectinload(Review.product)
            )
            .filter(Review.user_id == user_id)
            .all()
        )