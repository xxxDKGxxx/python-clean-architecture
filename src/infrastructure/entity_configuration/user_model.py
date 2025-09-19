from sqlalchemy import Table, Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from src.core.entities.address import Address
from src.core.entities.user import User
from src.infrastructure.entity_configuration.base import metadata, mapper_registry

user_table = Table(
    "Users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("firstname", String(200), nullable=False),
    Column("lastname", String(200), nullable=False),
)

mapper_registry.map_imperatively(
    User,
    user_table,
    properties = {
        "addresses": relationship(Address, back_populates="user")
    }
)