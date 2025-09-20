from abc import ABC

from src.core.entities.user import User
from src.core.repository_base import Repository


class UserRepository(
    Repository[User],
    ABC):

    pass
