from typing import Sequence

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.artist import Artist
from schemas.artist import ArtistCreate, ArtistUpdate
from settings.db import get_db


class ArtistService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self) -> Sequence[Artist]:
        result = await self.db.execute(select(Artist))
        return result.scalars().all()

    async def get_by_id(self, artist_id: str) -> Artist | None:
        result = await self.db.execute(select(Artist).where(Artist.id == artist_id))
        return result.scalars().first()

    async def create(self, data: ArtistCreate) -> Artist:
        artist = Artist(**data.model_dump())

        self.db.add(artist)
        await self.db.commit()
        await self.db.refresh(artist)

        return artist

    async def update(
        self,
        artist_id: str,
        data: ArtistUpdate,
    ) -> Artist | None:
        artist = await self.get_by_id(artist_id)

        if not artist:
            return None

        for field, value in data.model_dump(
            exclude_unset=True,
        ).items():
            setattr(artist, field, value)

        self.db.add(artist)

        await self.db.commit()
        await self.db.refresh(artist)

        return artist

    async def delete(self, artist_id: str) -> bool:
        artist = await self.get_by_id(artist_id)

        if not artist:
            return False

        await self.db.delete(artist)
        await self.db.commit()

        return True


async def get_artist_service(
    db: AsyncSession = Depends(get_db),
) -> ArtistService:
    return ArtistService(db)
