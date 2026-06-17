import os
import shutil

from fastapi import (
    APIRouter,
    Depends,
    File,
    HTTPException,
    Request,
    UploadFile,
    status,
)
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.templating import Jinja2Templates

from schemas.track import TrackCreate, TrackRead
from services.tracks import TrackService, get_track_service

router = APIRouter(
    prefix="/tracks",
    tags=["Tracks"],
)

templates = Jinja2Templates(
    directory="templates",
)


@router.get(
    "/",
    response_model=list[TrackRead],
)
async def get_tracks(
    track_service: TrackService = Depends(
        get_track_service,
    ),
):
    return await track_service.get_all()


@router.get(
    "/player",
    response_class=HTMLResponse,
)
async def player(
    request: Request,
    track_service: TrackService = Depends(
        get_track_service,
    ),
):
    tracks = await track_service.get_all()

    return templates.TemplateResponse(
        request=request,
        name="player.html",
        context={
            "tracks": tracks,
        },
    )


@router.get(
    "/{track_id}/play",
)
async def play_track(
    track_id: str,
    track_service: TrackService = Depends(
        get_track_service,
    ),
):
    track = await track_service.get_by_id(track_id)

    if not track:
        raise HTTPException(
            status_code=404,
            detail="Track not found",
        )

    return FileResponse(
        path=track.file_path,
        media_type="audio/mpeg",
        filename=os.path.basename(track.file_path),
    )


@router.post(
    "/upload",
    response_model=TrackRead,
    status_code=status.HTTP_201_CREATED,
)
async def upload_track(
    title: str,
    album_id: str,
    genre: str,
    duration: int,
    file: UploadFile = File(...),
    track_service: TrackService = Depends(
        get_track_service,
    ),
):
    upload_dir = "uploads/music"

    os.makedirs(
        upload_dir,
        exist_ok=True,
    )

    file_path = f"{upload_dir}/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(
            file.file,
            buffer,
        )

    track = await track_service.create(
        TrackCreate(
            title=title,
            album_id=album_id,
            genre=genre,
            duration=duration,
            file_path=file_path,
        )
    )

    return track
