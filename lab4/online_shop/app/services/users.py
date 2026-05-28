from datetime import datetime
from typing import List

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.user import UserRegister, UserRead, UserUpdate, UserRole
from app.repository.users import UserRepository
from app.security import get_password_hash, verify_password


class UserService:
    def __init__(self, db: Session):
        self.repository = UserRepository(db)

    def get_all_users(self) -> List[UserRead]:
        users = self.repository.get_all()
        return [UserRead.model_validate(user) for user in users]

    def get_user_by_id(self, user_id: int) -> UserRead:
        user = self.repository.get_by_id(user_id)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with id {user_id} not found"
            )

        return UserRead.model_validate(user)

    def get_user_by_email(self, email: str):
        return self.repository.get_user_by_email(email)

    def create_user(self, user_data: UserRegister) -> UserRead:
        existing_user = self.repository.get_user_by_email(user_data.email)

        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Користувач з email '{user_data.email}' вже існує"
            )

        user = self.repository.create({
            "name": user_data.name,
            "surname": user_data.surname,
            "email": user_data.email,
            "phone_number": user_data.phone_number,
            "password_hash": get_password_hash(user_data.password),
            "role": "user",
            "created_at": datetime.utcnow()
        })

        return UserRead.model_validate(user)

    def update_user(self, user_id: int, user_data: UserUpdate) -> UserRead:
        existing_user = self.repository.get_by_id(user_id)

        if not existing_user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        update_data = user_data.model_dump(exclude_unset=True)

        if "password_hash" in update_data:
            update_data["password_hash"] = get_password_hash(update_data["password_hash"])

        updated_user = self.repository.update(user_id, update_data)

        return UserRead.model_validate(updated_user)

    def delete_user(self, user_id: int):
        user = self.repository.delete(user_id)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        return {"message": "User deleted successfully"}

    def authenticate_user(self, email: str, password: str):
        user = self.repository.get_user_by_email(email)

        if not user:
            return None

        if not verify_password(password, user.password_hash):
            return None

        return user

    def user_registration(self, user_data: UserRegister) -> UserRead:
        existing_user = self.repository.get_user_by_email(user_data.email)

        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Користувач з email '{user_data.email}' вже існує"
            )

        user = self.repository.create({
            "name": user_data.name,
            "surname": user_data.surname,
            "email": user_data.email,
            "phone_number": user_data.phone_number,
            "password_hash": get_password_hash(user_data.password),
            "role": "user",
            "created_at": datetime.utcnow()
        })

        return UserRead.model_validate(user)

    def change_user_role(self, user_id: int, role: UserRole) -> UserRead:
        user = self.repository.get_by_id(user_id)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        updated_user = self.repository.update(
            user_id,
            {"role": role.value}
        )

        return UserRead.model_validate(updated_user)