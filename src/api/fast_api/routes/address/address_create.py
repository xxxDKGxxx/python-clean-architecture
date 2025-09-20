from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session

from src.api.dtos.address.create_address_request_dto import CreateAddressRequestDto
from src.api.dtos.address.create_address_response_dto import CreateAddressResponseDto
from src.api.fast_api.exception_converter import convert_to_http_exception
from src.infrastructure.database import get_db
from src.infrastructure.repositories.sql_alchemy_address_repository import SqlAlchemyAddressRepository
from src.use_cases.address.create_address.create_address_command import CreateAddressCommand
from src.use_cases.address.create_address.create_address_use_case import CreateAddressUseCase

router = APIRouter(prefix="/addresses")

@router.post(
    "/",
    response_model=CreateAddressResponseDto
)
async def create_address(
        address: CreateAddressRequestDto,
        session: Session = Depends(get_db)):

    command = CreateAddressCommand(
        address.street,
        address.city,
        address.userid
    )

    addresses_repository = SqlAlchemyAddressRepository(session)

    handler = CreateAddressUseCase(
        addresses_repository,
        command
    )

    try:
        new_address = handler.execute()
    except Exception as e:
        raise convert_to_http_exception(e)

    return CreateAddressResponseDto(
        id=new_address.id,
        street=new_address.street,
        city=new_address.city,
        userid=new_address.userid
    )


