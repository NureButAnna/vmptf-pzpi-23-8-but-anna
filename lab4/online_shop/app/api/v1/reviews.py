from fastapi import APIRouter, Depends, status

from app.models import User
from app.schemas.review import ReviewCreate, ReviewRead, ReviewUpdate
from app.services.reviews import ReviewService
from app.dependency import get_review_service, get_current_user, require_role

router = APIRouter(
    prefix="/reviews",
    tags=["Review🧐️"]
)

@router.get("/", response_model=list[ReviewRead])
def get_reviews(service: ReviewService = Depends(get_review_service)):
    return service.get_all_reviews()


@router.get("/{review_id}", response_model=ReviewRead)
def get_review(
    review_id: int,
    service: ReviewService = Depends(get_review_service)
):
    return service.get_review_by_id(review_id)


@router.get("/product/{product_id}", response_model=list[ReviewRead])
def get_reviews_by_product(
    product_id: int,
    service: ReviewService = Depends(get_review_service)
):
    return service.get_reviews_by_product(product_id)


@router.post("/", response_model=ReviewRead, status_code=status.HTTP_201_CREATED)
def create_review(
    review_data: ReviewCreate,
    service: ReviewService = Depends(get_review_service),
    current_user: User = Depends(require_role("користувач"))
):
    return service.create_review(review_data)


@router.put("/{review_id}", response_model=ReviewRead)
def update_review(
    review_id: int,
    review_data: ReviewUpdate,
    service: ReviewService = Depends(get_review_service),
    current_user: User = Depends(require_role("адмін", "менеджер"))
):
    return service.update_review(review_id, review_data)


@router.delete("/{review_id}", status_code=status.HTTP_200_OK)
def delete_review(
    review_id: int,
    service: ReviewService = Depends(get_review_service),
    current_user: User = Depends(require_role("адмін", "менеджер"))
):
    return service.delete_review(review_id)