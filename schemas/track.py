from datetime import datetime

from pydantic import BaseModel


class TrackCreate(BaseModel):
    title: str
    album_id: str
    genre: str
    duration: int
    file_path: str


class TrackRead(BaseModel):
    id: str
    title: str
    album_id: str
    genre: str
    duration: int
    file_path: str
    created_at: datetime

    model_config = {
        "from_attributes": True,
    }
