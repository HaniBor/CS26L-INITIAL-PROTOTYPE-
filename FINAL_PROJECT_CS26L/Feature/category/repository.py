from database.database import Database

class CategoryRepository:
    """Data access layer for categories stored in SQLite."""

    def __init__(self, db: Database):
        self.db = db

    def get_all(self):
        with self.db.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, name FROM categories ORDER BY name ASC")
            return cursor.fetchall()

    def get_by_name(self, name):
        with self.db.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, name FROM categories WHERE name = ?", (name,))
            return cursor.fetchone()

    def create(self, name):
        with self.db.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO categories (name) VALUES (?)", (name,))
            conn.commit()
            return cursor.lastrowid

    def update(self, old_name, new_name):
        with self.db.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE categories SET name = ? WHERE name = ?", (new_name, old_name))
            conn.commit()

    def delete(self, name):
        with self.db.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM categories WHERE name = ?", (name,))
            conn.commit()