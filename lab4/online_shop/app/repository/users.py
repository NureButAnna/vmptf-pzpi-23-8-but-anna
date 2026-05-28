from app.models.user import User
from app.repository.base import BaseRepository


class UserRepository(BaseRepository):
    model = User

    def get_user_by_email(self, email: str):
        return (
            self.db.query(User)
            .filter(User.email == email)
            .first()
        )
