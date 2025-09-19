from abc import ABC
from abc import abstractmethod
from typing import TypeVar, Generic

T = TypeVar("T")

class Repository(Generic[T], ABC):
    @abstractmethod
    def create(self, item: T) -> T:
        pass

    @abstractmethod
    def get_by_id(self, ident: int):
        pass
