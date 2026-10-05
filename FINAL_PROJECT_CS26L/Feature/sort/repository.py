from database.database import Database

class SortRepository:
    """Data access layer serving sort features."""

    def __init__(self, db: Database):
        self.db = db

    def get_all_data(self):
        with self.db.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, deadline, priority, status FROM tasks")
            return cursor.fetchall()