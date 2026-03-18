import sqlite3
from pathlib import Path
from typing import Literal
from pydantic import Field, DirectoryPath, FilePath
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    ENV: Literal["local", "dev", "prod"] = Field(default="local")
    OPEN_API_KEY: str = Field(..., alias="OPEN_API_KEY")
    GOOGLE_API_KEY: str = Field(..., alias="GOOGLE_API_KEY")
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


def init_db():
    config.DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(config.DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
                CREATE TABLE IF NOT EXISTS market_logs(
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                           sentiment_score REAL,
                           raw_data TEXT
                           )
                        """
        )
        conn.commit()
        print(f"[시스템] DB 준비완료 : {config.DB_PATH}")


if __name__ == "__main__":
    init_db()
