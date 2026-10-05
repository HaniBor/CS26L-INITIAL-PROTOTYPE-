import sqlite3
from pathlib import Path


class Database:
    def __init__(self, database_path: str | Path | None = None) -> None:
        # The database file is tasks.db in this folder.
        if database_path is None:
            database_path = Path(__file__).resolve().parent / "tasks.db"
        self.database_path = Path(database_path)

    # Opens a connection to the database file.
    def connect(self) -> sqlite3.Connection:
        connection = sqlite3.connect(self.database_path)
        connection.execute("PRAGMA foreign_keys = ON;")
        return connection

    # Creates the categories and tasks tables if they do not exist yet.
    # The with block saves the work and closes the file automatically.
    def create_tables(self) -> None:
        with self.connect() as connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS categories (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL UNIQUE
                );
                """
            )
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    category_id INTEGER NOT NULL,
                    name TEXT NOT NULL,
                    deadline TEXT NOT NULL,
                    priority TEXT NOT NULL DEFAULT 'LOW',
                    status TEXT NOT NULL DEFAULT 'PENDING',
                    FOREIGN KEY (category_id) REFERENCES categories (id) ON DELETE CASCADE
                );
                """
            )