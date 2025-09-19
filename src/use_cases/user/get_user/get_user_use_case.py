from urllib3 import request

from src.core.entities.user import User
from src.use_cases.exceptions import NotFoundError
from src.use_cases.repository_base import Repository
from src.use_cases.use_case_base import UseCaseBase
from src.use_cases.user.get_user.get_user_query import GetUserQuery


class GetUserUseCase(UseCaseBase):
    def __init__(
            self,
            users_repository: Repository[User],
            request: GetUserQuery
    ):
        self.users_repository = users_repository
        self.request = request


    def execute(self):
        user = self.users_repository.get_by_id(self.request.id)

        if user is None:
            raise NotFoundError(f"User with id {self.request.id} not found")

        return user
