from datetime import date
from enum import StrEnum

from pydantic import BaseModel, Field


class MediaStatus(StrEnum):
    WATCHED = "watched"
    WATCHING = "watching"
    PENDING = "pending"
    DROPPED = "dropped"


class Movie(BaseModel):
    id: str
    title: str
    release_date: date | None = None
    genres: list[str] = Field(default_factory=list)
    duration_min: int | None = None
    overview: str | None = None
    popularity: float | None = None
    vote_average: float | None = None
    status: MediaStatus = MediaStatus.PENDING
    tmdb_id: int | None = None


class Episode(BaseModel):
    id: str
    title: str
    season_number: int
    episode_number: int
    air_date: date | None = None
    duration_min: int | None = None
    overview: str | None = None
    tmdb_id: int | None = None


class Series(BaseModel):
    id: str
    title: str
    first_air_date: date | None = None
    last_air_date: date | None = None
    genres: list[str] = Field(default_factory=list)
    total_episodes: int | None = None
    total_seasons: int | None = None
    overview: str | None = None
    popularity: float | None = None
    vote_average: float | None = None
    status: MediaStatus = MediaStatus.PENDING
    episodes: list[Episode] = Field(default_factory=list)
    tmdb_id: int | None = None
