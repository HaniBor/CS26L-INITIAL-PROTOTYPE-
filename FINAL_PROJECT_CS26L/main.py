import sys
import os
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database.database import Database

# Category Layer
from Feature.category.repository import CategoryRepository
from Feature.category.service import CategoryService, ALL_TITLES

# Task Layer
from Feature.task.repository import TaskRepository
from Feature.task.service import TaskService
from Feature.task.view import task_form

# Search Layer
from Feature.search.repository import SearchRepository
from Feature.search.service import SearchService
from Feature.search.view import SearchView
from Feature.search.model import SearchCriteria

# Sort Layer
from Feature.sort.repository import SortRepository
from Feature.sort.service import SortService
from Feature.sort.view import SortView


class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Organizer and Tracker System")
        self.root.geometry("1000x550")
        self.root.minsize(860, 450)
        self.root.protocol("WM_DELETE_WINDOW", self.on_exit)

        self.selected_title = None
        self.row_map = {}

        # Initialize SQLite Database & Create Tables
        self.db = Database()
        self.db.create_tables()

        # Initialize Repositories and Services
        self.cat_repo = CategoryRepository(self.db)
        self.cat_service = CategoryService(self.cat_repo)

        self.task_repo = TaskRepository(self.db)
        self.task_service = TaskService(self.task_repo)

        self.search_repo = SearchRepository(self.db)
        self.search_service = SearchService(self.search_repo)

        self.sort_repo = SortRepository(self.db)
        self.sort_service = SortService(self.sort_repo)

        self.build_ui()
        self.refresh_titles()

    def build_ui(self):
        main = ttk.Frame(self.root, padding=10)
        main.pack(fill="both", expand=True)
        main.columnconfigure(1, weight=1)
        main.rowconfigure(0, weight=1)

        # Left Column: Category / Title Panel
        left = ttk.LabelFrame(main, text="Titles", padding=8)
        left.grid(row=0, column=0, sticky="ns", padx=(0, 10))

        self.title_list = tk.Listbox(left, width=24, exportselection=False, activestyle="none")
        self.title_list.pack(fill="both", expand=True)
        self.title_list.bind("<<ListboxSelect>>", self.on_title_select)

        title_buttons = ttk.Frame(left)
        title_buttons.pack(fill="x", pady=(8, 0))
        ttk.Button(title_buttons, text="New", width=7, command=self.new_title).pack(side="left")
        ttk.Button(title_buttons, text="Rename", width=7, command=self.rename_selected_title).pack(side="left", padx=4)
        ttk.Button(title_buttons, text="Delete", width=7, command=self.delete_selected_title).pack(side="left")

        # Right Column: Tasks Display Panel
        right = ttk.LabelFrame(main, text="Tasks", padding=8)
        right.grid(row=0, column=1, sticky="nsew")
        right.columnconfigure(0, weight=1)
        right.rowconfigure(1, weight=1)
        self.right_frame = right

        # Top Control Bar (Sort + Search Views)
        controls = ttk.Frame(right)
        controls.grid(row=0, column=0, columnspan=2, sticky="ew", pady=(0, 8))

        self.sort_view = SortView(controls, self.refresh_table)
        self.sort_view.pack(side="left", padx=(0, 10))

        self.search_view = SearchView(controls, self.refresh_table)
        self.search_view.pack(side="left")

        # Main Table Display
        columns = ("Title", "Task", "Deadline", "Priority", "Status")
        self.columns = columns
        self.tree = ttk.Treeview(right, columns=columns, show="headings", selectmode="browse")
        widths = {"Title": 120, "Task": 240, "Deadline": 100, "Priority": 80, "Status": 100}
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=widths[col], anchor="w")

        scroll = ttk.Scrollbar(right, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scroll.set)
        self.tree.grid(row=1, column=0, sticky="nsew")
        scroll.grid(row=1, column=1, sticky="ns")

        # Task Action Toolbar
        task_buttons = ttk.Frame(right)
        task_buttons.grid(row=2, column=0, columnspan=2, sticky="w", pady=(8, 0))
        ttk.Button(task_buttons, text="Add task", command=self.add_task_clicked).pack(side="left")
        ttk.Button(task_buttons, text="Edit task", command=self.edit_task_clicked).pack(side="left", padx=4)
        ttk.Button(task_buttons, text="Delete task", command=self.delete_task_clicked).pack(side="left")
        ttk.Button(task_buttons, text="Mark completed", command=self.complete_task_clicked).pack(side="left", padx=4)

        ttk.Button(main, text="Exit", command=self.on_exit).grid(row=1, column=1, sticky="e", pady=(8, 0))

    # --- Title Selection & Operations ---
    def refresh_titles(self, select=None):
        self.title_list.delete(0, "end")
        self.title_list.insert("end", ALL_TITLES)

        categories = self.cat_service.get_all_categories()
        for name in categories:
            self.title_list.insert("end", name)

        if select in categories:
            self.title_list.selection_set(categories.index(select) + 1)
            self.selected_title = select
        else:
            self.title_list.selection_set(0)
            self.selected_title = None

        self.refresh_table()

    def on_title_select(self, event=None):
        selection = self.title_list.curselection()
        if not selection:
            return
        self.selected_title = None if selection[0] == 0 else self.title_list.get(selection[0])
        self.refresh_table()

    def new_title(self):
        name = simpledialog.askstring("New title", "Title name:", parent=self.root)
        if name is None:
            return
        ok, msg = self.cat_service.create_category(name)
        if not ok:
            messagebox.showerror("Cannot create title", msg)
            return
        self.refresh_titles(select=name.strip())

    def rename_selected_title(self):
        if not self.need_title():
            return
        new_name = simpledialog.askstring("Rename title", "New title name:",
                                          initialvalue=self.selected_title, parent=self.root)
        if new_name is None:
            return
        ok, msg = self.cat_service.rename_category(self.selected_title, new_name)
        if not ok:
            messagebox.showerror("Cannot rename title", msg)
            return
        self.refresh_titles(select=new_name.strip())

    def delete_selected_title(self):
        if not self.need_title():
            return
        if messagebox.askyesno("Delete title", f"Delete '{self.selected_title}' and all its tasks?"):
            self.cat_service.delete_category(self.selected_title)
            self.refresh_titles()

    # --- Task Action Handlers ---
    def add_task_clicked(self):
        if not self.need_title():
            return
        values = task_form(self.root, "Add task")
        if values:
            self.task_service.add_task(
                self.selected_title, values["name"], values["deadline"],
                values["priority"], values["status"]
            )
            self.refresh_table()

    def edit_task_clicked(self):
        task_id = self.selected_task_id()
        if task_id is None:
            return
        current_task = self.task_service.get_task(task_id)
        if not current_task:
            return

        values = task_form(self.root, "Edit task", current_task)
        if values:
            self.task_service.update_task(
                task_id, values["name"], values["deadline"],
                values["priority"], values["status"]
            )
            self.refresh_table()

    def delete_task_clicked(self):
        task_id = self.selected_task_id()
        if task_id is None:
            return
        current_task = self.task_service.get_task(task_id)
        task_name = current_task["Task"] if current_task else "this task"

        if messagebox.askyesno("Delete task", f"Delete '{task_name}'?"):
            self.task_service.delete_task(task_id)
            self.refresh_table()

    def complete_task_clicked(self):
        task_id = self.selected_task_id()
        if task_id is None:
            return
        self.task_service.mark_completed(task_id)
        self.refresh_table()

    # --- Refresh Table ---
    def refresh_table(self):
        """Integrates search filtering and sorting results into Treeview."""
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.row_map = {}

        scope = self.selected_title
        scope_name = scope if scope is not None else "All titles"
        self.right_frame.config(text=f"Tasks - {scope_name}")
        self.tree.configure(displaycolumns="#all" if scope is None else self.columns[1:])

        # 1. Fetch search options & filter
        search_data = self.search_view.get_query_data()
        criteria = SearchCriteria(
            keyword=search_data["keyword"],
            status=search_data["status"],
            priority=search_data["priority"],
            scope=scope
        )
        filtered_rows = self.search_service.filter_tasks(criteria)

        # 2. Sort filtered items using SortService
        sort_option = self.sort_view.get_sort_option()
        final_rows = self.sort_service.sort_tasks(filtered_rows, sort_option)

        # 3. Populate Treeview
        for number, (title_name, task_id, task) in enumerate(final_rows):
            row_id = str(number)
            self.row_map[row_id] = task_id
            self.tree.insert("", "end", iid=row_id, values=(
                title_name,
                task.get("Task", ""),
                task.get("Deadline", ""),
                task.get("Priority", ""),
                task.get("Status", "")
            ))

    def need_title(self):
        if self.selected_title is None:
            messagebox.showinfo("Select a title", "Select a specific title on the left first (not 'All titles').")
            return False
        return True

    def selected_task_id(self):
        selection = self.tree.selection()
        if not selection:
            messagebox.showinfo("Select a task", "Select a task in the table first.")
            return None
        return self.row_map[selection[0]]

    def on_exit(self):
        if messagebox.askyesno("Exit", "Do you want to exit?"):
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()