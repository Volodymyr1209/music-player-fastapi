from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from models.base import Base


class Album(Base):
    __tablename__ = "albums"

    id: Mapped[str] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255))
    release_year: Mapped[int] = mapped_column(Integer)
    artist_id: Mapped[str] = mapped_column(ForeignKey("artists.id"))
    created_at: Mapped[str]
