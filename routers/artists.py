import logging
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.artist import Artist
from schemas.artist import ArtistCreate, ArtistRead, ArtistUpdate
from settings.db import get_db

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/artists", tags=["Artists"])

SessionDepend = Annotated[AsyncSession, Depends(get_db)]


@router.get("/", response_model=list[ArtistRead])
async def get_artists(session: SessionDepend):
    try:
        result = await session.execute(select(Artist))
        return result.scalars().all()

    except Exception as exc:
        logger.exception("Failed to get artists")

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to get artists",
        ) from exc


@router.post(
    "/",
    response_model=ArtistRead,
    status_code=status.HTTP_201_CREATED,
)
async def create_artist(
    artist_data: ArtistCreate,
    session: SessionDepend,
):
    try:
        artist = Artist(**artist_data.model_dump())

        session.add(artist)

        await session.commit()
        await session.refresh(artist)

        return artist

    except Exception as exc:
        logger.exception("Failed to create artist")

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create artist",
        ) from exc


@router.get(
    "/{artist_id}",
    response_model=ArtistRead,
)
async def get_artist(
    artist_id: str,
    session: SessionDepend,
):
    try:
        result = await session.execute(select(Artist).where(Artist.id == artist_id))

        artist = result.scalars().first()

        if not artist:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Artist not found",
            )

        return artist

    except HTTPException:
        raise

    except Exception as exc:
        logger.exception("Failed to get artist")

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to get artist",
        ) from exc


@router.put(
    "/{artist_id}",
    response_model=ArtistRead,
)
async def update_artist(
    artist_id: str,
    artist_update: ArtistUpdate,
    session: SessionDepend,
):
    try:
        result = await session.execute(select(Artist).where(Artist.id == artist_id))

        artist = result.scalars().first()

        if not artist:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Artist not found",
            )

        for field, value in artist_update.model_dump(exclude_unset=True).items():
            setattr(artist, field, value)

        await session.commit()
        await session.refresh(artist)

        return artist

    except HTTPException:
        raise

    except Exception as exc:
        logger.exception("Failed to update artist")

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to update artist",
        ) from exc


@router.delete(
    "/{artist_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_artist(
    artist_id: str,
    session: SessionDepend,
):
    try:
        result = await session.execute(select(Artist).where(Artist.id == artist_id))

        artist = result.scalars().first()

        if not artist:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Artist not found",
            )

        await session.delete(artist)
        await session.commit()

        return None

    except HTTPException:
        raise

    except Exception as exc:
        logger.exception("Failed to delete artist")

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to delete artist",
        ) from exc
