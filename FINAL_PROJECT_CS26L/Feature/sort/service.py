from Feature.sort.model import SortRule
from Feature.sort.repository import SortRepository

class SortService:
    """Business logic for task sorting algorithms."""

    def __init__(self, repository: SortRepository):
        self.repo = repository

    def sort_tasks(self, task_rows, sort_by="Added order"):
        """Sorts list of tuples [(title, task_id, task), ...] based on selected algorithm."""
        if sort_by == "Deadline":
            task_rows.sort(key=lambda item: SortRule.deadline_key(item[2]))
        elif sort_by == "Priority":
            task_rows.sort(key=lambda item: (
                SortRule.priority_key(item[2]),
                SortRule.deadline_key(item[2])
            ))
        return task_rows