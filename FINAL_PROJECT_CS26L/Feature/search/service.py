from Feature.search.model import SearchCriteria
from Feature.search.repository import SearchRepository

class SearchService:
    """Executes search and filtering business logic over SQLite records."""

    def __init__(self, repository: SearchRepository):
        self.repo = repository

    def filter_tasks(self, criteria: SearchCriteria):
        all_tasks = self.repo.get_all_tasks()
        filtered_rows = []
        keyword_lower = criteria.keyword

        for category_name, task_id, task in all_tasks:
            if criteria.scope is not None and category_name != criteria.scope:
                continue
            if criteria.status != "All" and task.get("Status") != criteria.status:
                continue
            if criteria.priority != "All" and task.get("Priority") != criteria.priority:
                continue
            if keyword_lower and keyword_lower not in task.get("Task", "").lower():
                continue
            filtered_rows.append((category_name, task_id, task))

        return filtered_rows