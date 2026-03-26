from datetime import date

from pydantic import BaseModel, Field


class Artist(BaseModel):
    id: str
    name: str
    genres: list[str] = Field(default_factory=list)
    popularity: int | None = None
    spotify_id: str | None = None
    lastfm_url: str | None = None


class Album(BaseModel):
    id: str
    title: str
    artist: Artist
    release_date: date | None = None
    total_tracks: int | None = None
    genres: list[str] = Field(default_factory=list)
    spotify_id: str | None = None


class Track(BaseModel):
    id: str
    title: str
    artist: Artist
    album: Album | None = None
    duration_ms: int | None = None
    popularity: int | None = None
    played_at: date | None = None
    spotify_id: str | None = None
    lastfm_url: str | None = None
