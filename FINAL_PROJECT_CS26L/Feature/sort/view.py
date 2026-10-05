import tkinter as tk
from tkinter import ttk

SORT_OPTIONS = ["Added order", "Deadline", "Priority"]

class SortView(ttk.Frame):
    """UI Component containing Sorting selection controls."""

    def __init__(self, parent, on_sort_change_callback):
        super().__init__(parent)
        self.on_change = on_sort_change_callback
        self.sort_var = tk.StringVar(value=SORT_OPTIONS[0])

        self.build_ui()

    def build_ui(self):
        ttk.Label(self, text="Sort by").pack(side="left")
        sort_cb = ttk.Combobox(self, textvariable=self.sort_var,
                               values=SORT_OPTIONS, state="readonly", width=12)
        sort_cb.pack(side="left", padx=(4, 8))
        sort_cb.bind("<<ComboboxSelected>>", lambda e: self.on_change())

    def get_sort_option(self):
        return self.sort_var.get()