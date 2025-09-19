from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.api.dtos.user.get_user.get_user_response_dto import GetUserResponseDto, AddressDto
from src.core.entities.user import User
from src.infrastructure.database import get_db
from src.infrastructure.repositories.sql_alchemy_repository import SqlAlchemyRepository
from src.use_cases.user.get_user.get_user_query import GetUserQuery
from src.use_cases.user.get_user.get_user_use_case import GetUserUseCase

router = APIRouter(prefix="/users")

@router.get("/{user_id}", response_model=GetUserResponseDto)
def get_user_by_id(
        user_id: int,
        session: Session = Depends(get_db)):

    query = GetUserQuery(user_id)

    repository = SqlAlchemyRepository[User](
        session,
        User
    )

    handler = GetUserUseCase(
        repository,
        query
    )

    user = handler.execute()

    return GetUserResponseDto(
        id=user.id,
        firstname=user.firstname,
        lastname=user.lastname,
        addresses=[AddressDto(
            id=adr.id,
            street=adr.street,
            city=adr.city
        ) for adr in user.addresses]
    )