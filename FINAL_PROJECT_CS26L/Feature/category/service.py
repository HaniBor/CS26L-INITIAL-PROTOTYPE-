from Feature.category.repository import CategoryRepository

ALL_TITLES = "[ All titles ]"

class CategoryService:
    """Business logic for Category/Title management operations using SQLite."""

    def __init__(self, repository: CategoryRepository):
        self.repo = repository

    def get_all_categories(self):
        records = self.repo.get_all()
        return [row[1] for row in records]

    def create_category(self, name):
        name = name.strip()
        if not name:
            return False, "Title cannot be empty."
        if name == ALL_TITLES:
            return False, "That name is reserved."
        
        existing = self.repo.get_by_name(name)
        if existing:
            return False, "TITLE ALREADY EXISTS!"
            
        self.repo.create(name)
        return True, ""

    def rename_category(self, old_name, new_name):
        new_name = new_name.strip()
        if not new_name:
            return False, "Title cannot be empty."
        if new_name == ALL_TITLES:
            return False, "That name is reserved."
        
        existing = self.repo.get_by_name(new_name)
        if existing and new_name != old_name:
            return False, "TITLE ALREADY EXISTS!"
            
        self.repo.update(old_name, new_name)
        return True, ""

    def delete_category(self, name):
        existing = self.repo.get_by_name(name)
        if existing:
            self.repo.delete(name)
            return True
        return False