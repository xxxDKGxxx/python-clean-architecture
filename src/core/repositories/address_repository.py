from abc import ABC

from src.core.entities.address import Address
from src.core.repository_base import Repository


class AddressRepository(
    Repository[Address],
    ABC):

    pass