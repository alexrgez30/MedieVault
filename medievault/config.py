from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    # Database
    database_url: str = "postgresql://localhost:5432/medievault"

    # Spotify
    spotify_client_id: str = ""
    spotify_client_secret: str = ""

    # TMDB
    tmdb_api_key: str = ""
    tmdb_base_url: str = "https://api.themoviedb.org/3"

    # Last.fm
    lastfm_api_key: str = ""
    lastfm_base_url: str = "https://ws.audioscrobbler.com/2.0"

    # OpenLibrary
    openlibrary_base_url: str = "https://openlibrary.org"

    # IGDB
    igdb_client_id: str = ""
    igdb_client_secret: str = ""
    igdb_base_url: str = "https://api.igdb.com/v4"

    # Prefect
    prefect_api_url: str = "http://localhost:4200/api"


settings = Settings()
