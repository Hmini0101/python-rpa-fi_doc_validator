import sqlite3
from config.settings import config


class DBManager:
    def __init__(self):
        self.db_path = config.DB_PATH

    def init_tables(self):
        with sqlite3.connect(self.db_path) as conn:
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

            cursor.execute(
                """
                    CREATE TABLE IF NOT EXISTS processed_docs(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        doc_type TEXT,
                        amount REAL,
                        currency TEXT,
                        doc_date TEXT,
                        account_number TEXT,
                        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
                    )
            """
            )
            conn.commit()
            print(f"[DB] 시슽템 테이블 준비완료: {self.db_path}")

    def insert_doc(self, data):
        """검증된 데이터를 DB에 삽입 (Pydantic 객체를 받음)"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO processed_docs(doc_type, amount, currency, doc_date, account_number)
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    data.doc_type,
                    data.amount,
                    data.currency,
                    str(data.doc_date),
                    data.account_number,
                ),
            )
            conn.commit()
            print(f"[DB] 데이터 저장 성공: {data.doc_type}")
