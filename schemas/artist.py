from typing import Optional

from pydantic import BaseModel, Field


class ArtistCreate(BaseModel):
    name: str = Field(max_length=255)
    country: str = Field(max_length=255)


class ArtistRead(BaseModel):
    id: str
    name: str
    country: str

    class Config:
        from_attributes = True


class ArtistUpdate(BaseModel):
    name: Optional[str] = Field(default=None, max_length=255)
    country: Optional[str] = Field(default=None, max_length=255)
