from sqlalchemy.orm import Session

from src.core.entities.address import Address
from src.core.repositories.address_repository import AddressRepository
from src.infrastructure.repositories.sql_alchemy_repository import SqlAlchemyRepository


class SqlAlchemyAddressRepository(
    AddressRepository,
    SqlAlchemyRepository):

    def __init__(
            self,
            session: Session):

        super().__init__(
            session,
            Address
        )

