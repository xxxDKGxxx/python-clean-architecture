from fastapi import APIRouter, Depends

from src.api.dtos.user.create_user.create_user_request_dto import CreateUserRequestDto
from src.api.dtos.user.create_user.create_user_response_dto import CreateUserResponseDto
from src.core.entities.user import User
from src.infrastructure.database import get_db
from src.infrastructure.repositories.sql_alchemy_repository import SqlAlchemyRepository
from src.use_cases.user.create_user.create_user_command import CreateUserCommand
from src.use_cases.user.create_user.create_user_use_case import CreateUserUseCase

router = APIRouter(prefix="/users")

@router.post(
    "/",
    response_model=CreateUserResponseDto
)

async def create_user(
        user: CreateUserRequestDto,
        session = Depends(get_db)
):

    command = CreateUserCommand(
        user.firstname,
        user.lastname
    )

    repository = SqlAlchemyRepository[User](session, User)

    handler = CreateUserUseCase(
        repository,
        command
    )

    new_user = handler.execute()

    return CreateUserResponseDto(
        id=new_user.id,
        firstname=new_user.firstname,
        lastname=new_user.lastname
    )
