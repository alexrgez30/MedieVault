from datetime import date
from enum import StrEnum

from pydantic import BaseModel, Field


class ReadStatus(StrEnum):
    READ = "read"
    READING = "reading"
    PENDING = "pending"
    ABANDONED = "abandoned"


class Author(BaseModel):
    id: str
    name: str
    birth_date: date | None = None
    bio: str | None = None
    openlibrary_id: str | None = None


class Book(BaseModel):
    id: str
    title: str
    authors: list[Author] = Field(default_factory=list)
    publish_date: date | None = None
    genres: list[str] = Field(default_factory=list)
    pages: int | None = None
    overview: str | None = None
    status: ReadStatus = ReadStatus.PENDING
    openlibrary_id: str | None = None
    isbn: str | None = None
