from typing import Sequence

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.track import Track
from schemas.track import TrackCreate
from settings.db import get_db


class TrackService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self) -> Sequence[Track]:
        result = await self.db.execute(select(Track))
        return result.scalars().all()

    async def get_by_id(self, track_id: str) -> Track | None:
        result = await self.db.execute(select(Track).where(Track.id == track_id))
        return result.scalars().first()

    async def create(self, data: TrackCreate) -> Track:
        track = Track(**data.model_dump())

        self.db.add(track)

        await self.db.commit()
        await self.db.refresh(track)

        return track


async def get_track_service(
    db: AsyncSession = Depends(get_db),
) -> TrackService:
    return TrackService(db)
