from database.database import Database

class TaskRepository:
    """Handles SQLite operations for task items."""

    def __init__(self, db: Database):
        self.db = db

    def add_task(self, category_name, name, deadline, priority, status):
        with self.db.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id FROM categories WHERE name = ?", (category_name,))
            cat_row = cursor.fetchone()
            if cat_row:
                cat_id = cat_row[0]
                cursor.execute(
                    """
                    INSERT INTO tasks (category_id, name, deadline, priority, status)
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    (cat_id, name, deadline, priority, status)
                )
                conn.commit()

    def update_task(self, task_id, name, deadline, priority, status):
        with self.db.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                UPDATE tasks
                SET name = ?, deadline = ?, priority = ?, status = ?
                WHERE id = ?
                """,
                (name, deadline, priority, status, task_id)
            )
            conn.commit()

    def delete_task(self, task_id):
        with self.db.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
            conn.commit()

    def update_status(self, task_id, status):
        with self.db.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE tasks SET status = ? WHERE id = ?", (status, task_id))
            conn.commit()

    def get_task_by_id(self, task_id):
        with self.db.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, deadline, priority, status FROM tasks WHERE id = ?", (task_id,))
            row = cursor.fetchone()
            if row:
                return {
                    "id": row[0],
                    "Task": row[1],
                    "Deadline": row[2],
                    "Priority": row[3],
                    "Status": row[4]
                }
            return None