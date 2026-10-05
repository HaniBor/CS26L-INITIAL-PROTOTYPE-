from database.database import Database

class SearchRepository:
    """Fetches task records from SQLite for query and filter operations."""

    def __init__(self, db: Database):
        self.db = db

    def get_all_tasks(self):
        with self.db.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT c.name, t.id, t.name, t.deadline, t.priority, t.status
                FROM tasks t
                JOIN categories c ON t.category_id = c.id
                """
            )
            rows = cursor.fetchall()
            
            result = []
            for r in rows:
                result.append((
                    r[0],  # Category Name
                    r[1],  # Task ID
                    {
                        "Task": r[2],
                        "Deadline": r[3],
                        "Priority": r[4],
                        "Status": r[5]
                    }
                ))
            return result