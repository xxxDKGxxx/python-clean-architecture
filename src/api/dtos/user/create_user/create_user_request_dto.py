from pydantic import BaseModel


class CreateUserRequestDto(BaseModel):
    firstname: str
    lastname: str
