import tkinter as tk
from tkinter import ttk

class SearchView(ttk.Frame):
    """UI Component containing Search & Filter controls."""

    def __init__(self, parent, on_search_change_callback):
        super().__init__(parent)
        self.on_change = on_search_change_callback

        self.status_var = tk.StringVar(value="All")
        self.priority_var = tk.StringVar(value="All")
        self.search_var = tk.StringVar()

        self.build_ui()

    def build_ui(self):
        ttk.Label(self, text="Status").pack(side="left")
        status_cb = ttk.Combobox(self, textvariable=self.status_var,
                                 values=["All", "PENDING", "IN PROGRESS", "COMPLETED"],
                                 state="readonly", width=12)
        status_cb.pack(side="left", padx=(4, 8))
        status_cb.bind("<<ComboboxSelected>>", lambda e: self.on_change())

        ttk.Label(self, text="Priority").pack(side="left")
        priority_cb = ttk.Combobox(self, textvariable=self.priority_var,
                                   values=["All", "LOW", "MEDIUM", "HIGH"],
                                   state="readonly", width=9)
        priority_cb.pack(side="left", padx=(4, 8))
        priority_cb.bind("<<ComboboxSelected>>", lambda e: self.on_change())

        ttk.Label(self, text="Search").pack(side="left")
        entry = ttk.Entry(self, textvariable=self.search_var, width=18)
        entry.pack(side="left", padx=(4, 8))
        self.search_var.trace_add("write", lambda *args: self.on_change())

    def get_query_data(self):
        return {
            "status": self.status_var.get(),
            "priority": self.priority_var.get(),
            "keyword": self.search_var.get()
        }