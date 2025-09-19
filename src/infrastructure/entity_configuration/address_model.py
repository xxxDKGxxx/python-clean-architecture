from sqlalchemy import Table, Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship

from src.core.entities.address import Address
from src.core.entities.user import User
from src.infrastructure.entity_configuration.base import metadata, mapper_registry

addresses_table = Table(
    "Addresses",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("street", Text, nullable=False),
    Column("city", Text, nullable=False),
    Column("userid", Integer, ForeignKey("Users.id"), nullable=False)
)

mapper_registry.map_imperatively(
    Address,
    addresses_table,
    properties = {
        "user": relationship(User, back_populates="addresses")
    }
)

