from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from models.base import Base


class PlaylistTrack(Base):
    __tablename__ = "playlist_tracks"

    playlist_id: Mapped[str] = mapped_column(
        ForeignKey("playlists.id"),
        primary_key=True,
    )

    track_id: Mapped[str] = mapped_column(
        ForeignKey("tracks.id"),
        primary_key=True,
    )
