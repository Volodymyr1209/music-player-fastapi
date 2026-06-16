import logging

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import FileResponse

from schemas.artist import ArtistCreate, ArtistRead, ArtistUpdate
from services.artists import ArtistService, get_artist_service
from services.pdf_generator import generate_artist_report

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/artists", tags=["Artists"])


@router.get("/", response_model=list[ArtistRead])
async def get_artists(
    artist_service: ArtistService = Depends(get_artist_service),
):
    try:
        return await artist_service.get_all()

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
    artist_service: ArtistService = Depends(get_artist_service),
):
    try:
        return await artist_service.create(artist_data)

    except Exception as exc:
        logger.exception("Failed to create artist")

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create artist",
        ) from exc


@router.get("/report")
async def get_artists_report(
    artist_service: ArtistService = Depends(get_artist_service),
):
    try:
        artists = await artist_service.get_all()

        artist_lines = [f"{artist.name} ({artist.country})" for artist in artists]

        pdf_path = generate_artist_report(
            "artists_report.pdf",
            artist_lines,
        )

        return FileResponse(
            path=pdf_path,
            filename="artists_report.pdf",
            media_type="application/pdf",
        )

    except Exception as exc:
        logger.exception("Failed to generate report")

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to generate report",
        ) from exc


@router.get(
    "/{artist_id}",
    response_model=ArtistRead,
)
async def get_artist(
    artist_id: str,
    artist_service: ArtistService = Depends(get_artist_service),
):
    try:
        artist = await artist_service.get_by_id(artist_id)

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
    artist_service: ArtistService = Depends(get_artist_service),
):
    try:
        artist = await artist_service.update(
            artist_id,
            artist_update,
        )

        if not artist:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Artist not found",
            )

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
    artist_service: ArtistService = Depends(get_artist_service),
):
    try:
        deleted = await artist_service.delete(artist_id)

        if not deleted:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Artist not found",
            )

        return None

    except HTTPException:
        raise

    except Exception as exc:
        logger.exception("Failed to delete artist")

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to delete artist",
        ) from exc
