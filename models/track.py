from datetime import datetime
from uuid import uuid4

from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from models.base import Base


class Track(Base):
    __tablename__ = "tracks"

    id: Mapped[str] = mapped_column(
        String,
        primary_key=True,
        default=lambda: str(uuid4()),
    )

    title: Mapped[str] = mapped_column(
        String(255),
    )

    album_id: Mapped[str] = mapped_column(
        ForeignKey("albums.id"),
    )

    genre: Mapped[str] = mapped_column(
        String(100),
    )

    duration: Mapped[int] = mapped_column(
        Integer,
    )

    file_path: Mapped[str] = mapped_column(
        String(255),
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )
