import sqlite3
from pathlib import Path
from typing import Literal
from pydantic import Field, DirectoryPath, FilePath
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    ENV: Literal["local", "dev", "prod"] = Field(default="local")
    # 클로드키(임시)
    OPEN_API_KEY: str = Field(..., alias="OPEN_API_KEY")
    # 구글키
    GOOGLE_API_KEY: str = Field(default=None)
    OCR_THRESHOLD: float = Field(default=0.8, ge=0.0, le=1.0)

    BASE_DIR: Path = Path(__file__).resolve().parent.parent
    DB_PATH: Path = Field(default=BASE_DIR / "data" / "finance_data.db")
    DATA_RAW_DIR: Path = Field(default=BASE_DIR / "logs")

    model_config = SettingsConfigDict(
        env_file=Path(__file__).resolve().parent.parent / ".env",  # 절대 경로로 지정
        env_file_encoding="utf-8",
        extra="ignore",
    )


config = Settings()
