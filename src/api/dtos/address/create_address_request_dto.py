from pydantic import BaseModel

class CreateAddressRequestDto(BaseModel):
    street: str
    city: str
    userid: int