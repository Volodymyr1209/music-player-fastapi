from uuid import uuid4

from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column

from models.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(
        String,
        primary_key=True,
        default=lambda: str(uuid4()),
    )

    username: Mapped[str] = mapped_column(
        String(100),
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
    )

    password_hash: Mapped[str] = mapped_column(
        String(255),
    )

    role: Mapped[str] = mapped_column(
        String(50),
        server_default="user",
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        server_default="true",
    )
