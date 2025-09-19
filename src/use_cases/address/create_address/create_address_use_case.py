from src.core.entities.address import Address
from src.core.entities.user import User
from src.use_cases.address.create_address.create_address_command import CreateAddressCommand
from src.use_cases.repository_base import Repository
from src.use_cases.use_case_base import UseCaseBase


class CreateAddressUseCase(UseCaseBase):
    def __init__(
            self,
            addresses_repository: Repository[Address],
            request: CreateAddressCommand):
        self.addresses_repository = addresses_repository
        self.request = request

    def execute(self):

        new_address = Address(
            street=self.request.street,
            city=self.request.city,
            userid=self.request.userid
        )

        new_address = (self.addresses_repository.create(new_address))

        return new_address

