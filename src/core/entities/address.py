from typing import Optional

from .base import EntityBase
from src.core.entities.user import User



class Address(EntityBase):
    street: str
    city: str
    userid: int
    user: Optional[User]

    def __init__(
            self,
            street: str,
            city: str,
            userid: int):

        self.street = street
        self.city = city
        self.userid = userid