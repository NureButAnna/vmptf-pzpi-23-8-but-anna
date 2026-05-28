from http.client import HTTPException
from sqlalchemy.orm import Session

from app.models import User
from app.repository.users import UserRepository
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from app.security import decode_access_token
from app.database import get_db
from app.repository import users as user_repository
from app.services.products import ProductService
from app.services.users import UserService
from app.services.orders import OrderService
from app.services.reviews import ReviewService
from app.services.categories import CategoryService

from fastapi import Depends

def get_order_service(db=Depends(get_db)) -> OrderService:
    return OrderService(db)


def get_user_service(db=Depends(get_db)) -> UserService:
    return UserService(db)


def get_product_service(db=Depends(get_db)) -> ProductService:
    return ProductService(db)


def get_review_service(db=Depends(get_db)) -> ReviewService:
    return ReviewService(db)


def get_category_service(db=Depends(get_db)) -> CategoryService:
    return CategoryService(db)


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    payload = decode_access_token(token)

    if payload is None:
        raise credentials_exception

    email: str = payload.get("sub")

    if email is None:
        raise credentials_exception

    service = UserService(db)

    user = service.get_user_by_email(email)

    if user is None:
        raise credentials_exception

    return user


def require_role(*allowed_roles):
    def checker(current_user: User = Depends(get_current_user)):
        if current_user.role not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Forbidden"
            )
        return current_user
    return checker
