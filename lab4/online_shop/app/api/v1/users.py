from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.dependency import get_current_user, require_role
from app.models import User
from app.schemas.user import UserRegister, UserRead, UserUpdate, UserRole
from app.services.users import UserService

router = APIRouter(
    prefix="/users",
    tags=["User 👤"]
)

@router.get("/me", response_model=UserRead)
def get_me(current_user: User = Depends(get_current_user)):
    return current_user


@router.patch("/{user_id}/role", response_model=UserRead)
def update_role(
    user_id: int,
    role: UserRole,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role("адмін", "менеджер"))
):
    service = UserService(db)
    return service.change_user_role(user_id, role)


@router.get("/", response_model=list[UserRead], status_code=status.HTTP_200_OK)
def get_users(db: Session = Depends(get_db)):
    service = UserService(db)
    return service.get_all_users()


@router.get("/{user_id}", response_model=UserRead)
def get_user(user_id: int, db: Session = Depends(get_db)):
    service = UserService(db)
    return service.get_user_by_id(user_id)


@router.put("/{user_id}", response_model=UserUpdate)
def update_user(
    user_id: int,
    user_data: UserUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role("користувач", "адмін", "менеджер"))
):

    service = UserService(db)

    return service.update_user(
        user_id=user_id,
        user_data=user_data
    )


@router.post("/",response_model=UserRegister, status_code=status.HTTP_201_CREATED)
def add_user(
    user_data: UserRegister,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role("адмін", "менеджер"))
):
    service = UserService(db)
    return service.create_user(user_data)


@router.delete("/{user_id}", status_code=status.HTTP_200_OK)
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role("адмін", "менеджер"))
):
    service= UserService(db)
    return service.delete_user(user_id)

