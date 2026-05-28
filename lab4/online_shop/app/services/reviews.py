from typing import List

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.review import ReviewCreate, ReviewRead, ReviewUpdate
from app.repository.reviews import ReviewRepository


class ReviewService:
    def __init__(self, db: Session):
        self.repository = ReviewRepository(db)

    def get_all_reviews(self) -> List[ReviewRead]:
        reviews = self.repository.get_all()
        return [ReviewRead.model_validate(r) for r in reviews]

    def get_review_by_id(self, review_id: int) -> ReviewRead:
        review = self.repository.get_by_id(review_id)

        if not review:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Review with id {review_id} not found"
            )

        return ReviewRead.model_validate(review)

    def get_reviews_by_product(self, product_id: int) -> List[ReviewRead]:
        reviews = self.repository.get_by_product_id(product_id)
        return [ReviewRead.model_validate(r) for r in reviews]

    def create_review(self, data: ReviewCreate) -> ReviewRead:
        review = self.repository.create(
            data.model_dump()
        )

        return ReviewRead.model_validate(review)

    def update_review(self, review_id: int, data: ReviewUpdate) -> ReviewRead:
        updated = self.repository.update(
            review_id,
            data.model_dump(exclude_unset=True)
        )

        if not updated:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Review with id {review_id} not found"
            )

        return ReviewRead.model_validate(updated)

    def delete_review(self, review_id: int):
        deleted = self.repository.delete(review_id)

        if not deleted:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Review with id {review_id} not found"
            )

        return {"message": "Review deleted successfully"}