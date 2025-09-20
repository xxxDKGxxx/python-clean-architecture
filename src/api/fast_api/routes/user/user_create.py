from fastapi import APIRouter, Depends

from src.api.dtos.user.create_user.create_user_request_dto import CreateUserRequestDto
from src.api.dtos.user.create_user.create_user_response_dto import CreateUserResponseDto
from src.api.fast_api.exception_converter import convert_to_http_exception
from src.infrastructure.database import get_db
from src.infrastructure.repositories.sql_alchemy_user_repository import SqlAlchemyUserRepository
from src.use_cases.user.create_user.create_user_command import CreateUserCommand
from src.use_cases.user.create_user.create_user_use_case import CreateUserUseCase

router = APIRouter(prefix="/users")

@router.post(
    "/",
    response_model=CreateUserResponseDto
)
async def create_user(
        user: CreateUserRequestDto,
        session = Depends(get_db)):

    command = CreateUserCommand(
        user.firstname,
        user.lastname
    )

    repository = SqlAlchemyUserRepository(session)

    handler = CreateUserUseCase(
        repository,
        command
    )

    try:
        new_user = handler.execute()
    except Exception as e:
        raise convert_to_http_exception(e)

    return CreateUserResponseDto(
        id=new_user.id,
        firstname=new_user.firstname,
        lastname=new_user.lastname
    )
