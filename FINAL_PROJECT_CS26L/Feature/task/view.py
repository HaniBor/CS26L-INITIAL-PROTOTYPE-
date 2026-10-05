import calendar
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date
from Feature.task.model import DATE_FORMAT, parse_deadline

MONTHS = list(calendar.month_name)[1:]
PRIORITIES = ["LOW", "MEDIUM", "HIGH"]
STATUSES = ["PENDING", "IN PROGRESS", "COMPLETED"]

class ScrollDatePicker(ttk.Frame):
    """UI Widget for selecting Month, Day, and Year."""

    def __init__(self, parent, initial=None, first_year=None, last_year=None):
        super().__init__(parent)
        today = date.today()
        initial = initial or today
        first_year = first_year or today.year
        last_year = last_year or today.year + 10

        self.month_var = tk.StringVar(value=MONTHS[initial.month - 1])
        self.day_var = tk.StringVar(value=str(initial.day))
        self.year_var = tk.StringVar(value=str(initial.year))

        self.month_cb = ttk.Combobox(self, textvariable=self.month_var, values=MONTHS, width=11, state="readonly")
        self.day_cb = ttk.Combobox(self, textvariable=self.day_var, width=4, state="readonly")
        self.year_cb = ttk.Combobox(self, textvariable=self.year_var, width=6, state="readonly",
                                    values=[str(y) for y in range(first_year, last_year + 1)])

        self.month_cb.grid(row=0, column=0, padx=2)
        self.day_cb.grid(row=0, column=1, padx=2)
        self.year_cb.grid(row=0, column=2, padx=2)

        self.month_cb.bind("<<ComboboxSelected>>", self._update_days)
        self.year_cb.bind("<<ComboboxSelected>>", self._update_days)
        self._update_days()

    def _update_days(self, event=None):
        month = MONTHS.index(self.month_var.get()) + 1
        year = int(self.year_var.get())
        days_in_month = calendar.monthrange(year, month)[1]
        self.day_cb["values"] = [str(d) for d in range(1, days_in_month + 1)]
        if int(self.day_var.get()) > days_in_month:
            self.day_var.set(str(days_in_month))

    def get_date(self):
        return date(int(self.year_var.get()), MONTHS.index(self.month_var.get()) + 1, int(self.day_var.get()))

def task_form(parent, heading, task=None):
    """Popup window for creating or editing tasks."""
    win = tk.Toplevel(parent)
    win.title(heading)
    win.transient(parent)
    win.resizable(False, False)

    original_deadline = parse_deadline(task["Deadline"]) if task else None
    initial = original_deadline or date.today()
    first_year = min(date.today().year, initial.year)
    last_year = max(date.today().year + 10, initial.year)

    name_var = tk.StringVar(value=task["Task"] if task else "")
    priority_var = tk.StringVar(value=task["Priority"] if task else "LOW")
    status_var = tk.StringVar(value=task["Status"] if task else "PENDING")

    form = ttk.Frame(win, padding=15)
    form.grid(row=0, column=0)

    ttk.Label(form, text="Task name").grid(row=0, column=0, sticky="w", pady=5)
    name_entry = ttk.Entry(form, textvariable=name_var, width=32)
    name_entry.grid(row=0, column=1, sticky="w", pady=5)

    ttk.Label(form, text="Deadline").grid(row=1, column=0, sticky="w", pady=5)
    picker = ScrollDatePicker(form, initial=initial, first_year=first_year, last_year=last_year)
    picker.grid(row=1, column=1, sticky="w", pady=5)

    ttk.Label(form, text="Priority").grid(row=2, column=0, sticky="w", pady=5)
    ttk.Combobox(form, textvariable=priority_var, values=PRIORITIES, state="readonly", width=15).grid(row=2, column=1, sticky="w", pady=5)

    ttk.Label(form, text="Status").grid(row=3, column=0, sticky="w", pady=5)
    ttk.Combobox(form, textvariable=status_var, values=STATUSES, state="readonly", width=15).grid(row=3, column=1, sticky="w", pady=5)

    result = {}

    def on_ok():
        name = name_var.get().strip()
        if not name:
            messagebox.showerror("Invalid input", "Task name cannot be empty.", parent=win)
            return
        chosen = picker.get_date()
        if chosen < date.today() and chosen != original_deadline:
            messagebox.showerror("Invalid deadline", "Deadline cannot be in the past.", parent=win)
            return
        result.update({
            "name": name,
            "deadline": chosen.strftime(DATE_FORMAT),
            "priority": priority_var.get(),
            "status": status_var.get(),
        })
        win.destroy()

    buttons = ttk.Frame(form)
    buttons.grid(row=4, column=0, columnspan=2, pady=(12, 0), sticky="e")
    ttk.Button(buttons, text="Save", command=on_ok).pack(side="left", padx=4)
    ttk.Button(buttons, text="Cancel", command=win.destroy).pack(side="left")

    name_entry.focus()
    win.grab_set()
    win.bind("<Return>", lambda e: on_ok())
    win.bind("<Escape>", lambda e: win.destroy())
    parent.wait_window(win)
    return result or None