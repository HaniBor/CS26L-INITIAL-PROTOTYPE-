from Feature.task.repository import TaskRepository

class TaskService:
    """Executes task management operations."""

    def __init__(self, repository: TaskRepository):
        self.repo = repository

    def add_task(self, category_name, name, deadline, priority, status):
        self.repo.add_task(category_name, name, deadline, priority, status)

    def update_task(self, task_id, name, deadline, priority, status):
        self.repo.update_task(task_id, name, deadline, priority, status)

    def delete_task(self, task_id):
        self.repo.delete_task(task_id)

    def mark_completed(self, task_id):
        self.repo.update_status(task_id, "COMPLETED")

    def get_task(self, task_id):
        return self.repo.get_task_by_id(task_id)