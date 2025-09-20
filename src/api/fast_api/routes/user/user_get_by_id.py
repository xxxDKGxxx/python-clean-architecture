from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.api.dtos.user.get_user.get_user_response_dto import GetUserResponseDto, AddressDto
from src.api.fast_api.exception_converter import convert_to_http_exception
from src.infrastructure.database import get_db
from src.infrastructure.repositories.sql_alchemy_user_repository import SqlAlchemyUserRepository
from src.use_cases.user.get_user.get_user_query import GetUserQuery
from src.use_cases.user.get_user.get_user_use_case import GetUserUseCase

router = APIRouter(prefix="/users")

@router.get("/{user_id}", response_model=GetUserResponseDto)
def get_user_by_id(
        user_id: int,
        session: Session = Depends(get_db)):

    query = GetUserQuery(user_id)

    repository = SqlAlchemyUserRepository(session)

    handler = GetUserUseCase(
        repository,
        query
    )

    try:
        user = handler.execute()
    except Exception as e:
        raise convert_to_http_exception(e)

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