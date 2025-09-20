from typing import TypeVar, Generic, Type

from sqlalchemy.orm import Session

from src.core.repository_base import Repository
from src.infrastructure.exceptions.exceptions import SessionNoneError

T = TypeVar("T")

class SqlAlchemyRepository(Generic[T], Repository[T]):
    def __init__(self, session: Session, entity_type: Type[T]):
        self.session = session
        self.entity_type = entity_type

    def create(self, item: T):
        if not self.session:
            raise SessionNoneError

        self.session.add(item)
        self.session.commit()
        self.session.refresh(item)

        return item

    def get_by_id(self, ident: int):
        return self.session.get(self.entity_type, ident)