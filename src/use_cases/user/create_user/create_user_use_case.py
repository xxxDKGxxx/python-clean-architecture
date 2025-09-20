from src.core.entities.user import User
from src.core.repositories.user_repository import UserRepository
from src.use_cases.use_case_base import UseCaseBase
from src.use_cases.user.create_user.create_user_command import CreateUserCommand


class CreateUserUseCase(UseCaseBase):
    def __init__(
            self,
            users_repository: UserRepository,
            request: CreateUserCommand):

        self.users_repository = users_repository
        self.request = request

    def execute(self):
        new_user = User(
            self.request.firstname,
            self.request.lastname
        )

        new_user = self.users_repository.create(new_user)

        return new_user





