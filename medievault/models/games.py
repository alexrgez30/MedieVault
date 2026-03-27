from datetime import date
from enum import StrEnum

from pydantic import BaseModel, Field


class PlayStatus(StrEnum):
    COMPLETED = "completed"
    PLAYING = "playing"
    PENDING = "pending"
    ABANDONED = "abandoned"


class Platform(BaseModel):
    id: str
    name: str
    igdb_id: int | None = None


class Game(BaseModel):
    id: str
    title: str
    platforms: list[Platform] = Field(default_factory=list)
    release_date: date | None = None
    genres: list[str] = Field(default_factory=list)
    overview: str | None = None
    popularity: float | None = None
    vote_average: float | None = None
    status: PlayStatus = PlayStatus.PENDING
    igdb_id: int | None = None
