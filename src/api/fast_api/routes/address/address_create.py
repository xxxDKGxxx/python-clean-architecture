from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session

from src.api.dtos.address.create_address_request_dto import CreateAddressRequestDto
from src.api.dtos.address.create_address_response_dto import CreateAddressResponseDto
from src.core.entities.address import Address
from src.core.entities.user import User
from src.infrastructure.database import get_db
from src.infrastructure.repositories.sql_alchemy_repository import SqlAlchemyRepository
from src.use_cases.address.create_address.create_address_command import CreateAddressCommand
from src.use_cases.address.create_address.create_address_use_case import CreateAddressUseCase

router = APIRouter(prefix="/addresses")

@router.post("/")
async def create_address(
        address: CreateAddressRequestDto,
        session: Session = Depends(get_db)):

    command = CreateAddressCommand(
        address.street,
        address.city,
        address.userid
    )

    addresses_repository = SqlAlchemyRepository[Address](session, Address)

    handler = CreateAddressUseCase(
        addresses_repository,
        command
    )

    new_address = handler.execute()

    return CreateAddressResponseDto(
        id=new_address.id,
        street=new_address.street,
        city=new_address.city,
        userid=new_address.userid
    )


