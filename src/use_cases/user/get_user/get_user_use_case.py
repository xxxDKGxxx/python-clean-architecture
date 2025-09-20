from src.core.repositories.user_repository import UserRepository
from src.use_cases.exceptions.exceptions import NotFoundError
from src.use_cases.use_case_base import UseCaseBase
from src.use_cases.user.get_user.get_user_query import GetUserQuery


class GetUserUseCase(UseCaseBase):
    def __init__(
            self,
            users_repository: UserRepository,
            request: GetUserQuery
    ):
        self.users_repository = users_repository
        self.request = request


    def execute(self):
        user = self.users_repository.get_by_id(self.request.id)

        if user is None:
            raise NotFoundError(f"User with id {self.request.id} not found")

        return user
