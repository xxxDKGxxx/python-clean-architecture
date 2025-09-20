from .base import EntityBase



class User(EntityBase):
    firstname: str
    lastname: str
    addresses = []

    def __init__(
            self,
            firstname: str,
            lastname: str):

        self.firstname = firstname
        self.lastname = lastname
