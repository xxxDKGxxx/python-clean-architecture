from sqlalchemy.orm import Session

from src.core.entities.user import User
from src.core.repositories.user_repository import UserRepository
from src.infrastructure.repositories.sql_alchemy_repository import SqlAlchemyRepository


class SqlAlchemyUserRepository(
    UserRepository,
    SqlAlchemyRepository):

    def __init__(
            self,
            session: Session):

        super().__init__(
            session,
            User
        )