# CS26L-INITIAL-PROTOTYPE-
# Task Organizer and Tracker System

## 1. Project Title

**Task Organizer and Tracker System**

---

## 2. Project Description

The **Task Organizer and Tracker System** is a desktop application developed in Python using Tkinter and SQLite. It allows users to organize their tasks using different titles or categories.

The system helps users manage their tasks in one place instead of keeping tasks in separate notes or lists. Users can create titles, add tasks under a title, set deadlines, assign priorities and statuses, edit tasks, delete tasks, and mark tasks as completed.

The system also provides search, filtering, and sorting functions to make it easier to find and organize tasks.

---

## 3. Project Objectives

The main objectives of the project are:

* To create a simple desktop task management system.
* To allow users to organize tasks using titles or categories.
* To store task information using a SQLite database.
* To provide Create, Read, Update, and Delete operations.
* To allow users to search and filter tasks.
* To allow users to sort tasks by deadline or priority.
* To apply Object-Oriented Programming concepts and a layered project structure.
* To provide a simple graphical user interface that is easy to use.

---

## 4. Features

### Title/Category Management

Users can:

* Create a new title.
* Rename an existing title.
* Delete a title.
* View all available titles.
* Select **[ All titles ]** to display tasks from all titles.

A title cannot be empty, duplicated, or named `[ All titles ]`.

### Task Management

Users can:

* Add a task.
* Edit a task.
* Delete a task.
* Mark a task as completed.
* View task information.

Each task contains:

* Task name
* Deadline
* Priority
* Status
* Title/category

### Deadline Selection

The task form provides a date picker where the user can select:

* Month
* Day
* Year

The system does not allow a new task to have a deadline in the past.

### Priority

Tasks can have one of the following priorities:

* LOW
* MEDIUM
* HIGH

### Status

Tasks can have one of the following statuses:

* PENDING
* IN PROGRESS
* COMPLETED

### Search and Filtering

The system allows users to:

* Search tasks by task name.
* Filter tasks by status.
* Filter tasks by priority.
* View tasks under a selected title.

### Sorting

Tasks can be sorted by:

* Added order
* Deadline
* Priority

When sorting by priority, the order is:

**HIGH → MEDIUM → LOW**

### SQLite Database

The system automatically creates the required SQLite tables when the application starts.

---

## 5. Technologies Used

| Technology | Purpose                                                     |
| ---------- | ----------------------------------------------------------- |
| Python     | Main programming language                                   |
| Tkinter    | Graphical User Interface                                    |
| ttk        | GUI widgets such as buttons, tables, frames, and comboboxes |
| SQLite     | Local database                                              |
| sqlite3    | Python library used to connect to SQLite                    |
| pathlib    | Used for handling the database file path                    |
| calendar   | Used by the date picker                                     |
| datetime   | Used for handling and comparing deadlines                   |

The project uses Python's standard libraries and does not require an external GUI or database package.

---

## 6. Project Structure

```text
FINAL_PROJECT_CS26L/
│
├── main.py
│
├── database/
│   └── database.py
│
└── Feature/
    │
    ├── category/
    │   ├── repository.py
    │   └── service.py
    │
    ├── task/
    │   ├── model.py
    │   ├── repository.py
    │   ├── service.py
    │   └── view.py
    │
    ├── search/
    │   ├── model.py
    │   ├── repository.py
    │   ├── service.py
    │   └── view.py
    │
    └── sort/
        ├── model.py
        ├── repository.py
        ├── service.py
        └── view.py
```

### File and Folder Descriptions

| File/Folder                      | Purpose                                                                  |
| -------------------------------- | ------------------------------------------------------------------------ |
| `main.py`                        | Starts the application and connects the different layers together.       |
| `database/database.py`           | Handles SQLite connections and creates the database tables.              |
| `Feature/category/`              | Handles title/category management.                                       |
| `Feature/category/repository.py` | Performs database operations for categories.                             |
| `Feature/category/service.py`    | Contains the business logic for creating, renaming, and deleting titles. |
| `Feature/task/`                  | Handles task management.                                                 |
| `Feature/task/model.py`          | Contains deadline parsing and date-related functions.                    |
| `Feature/task/repository.py`     | Performs database operations for tasks.                                  |
| `Feature/task/service.py`        | Handles task management operations.                                      |
| `Feature/task/view.py`           | Contains the task form and date picker GUI.                              |
| `Feature/search/`                | Handles searching and filtering tasks.                                   |
| `Feature/search/model.py`        | Stores search criteria.                                                  |
| `Feature/search/repository.py`   | Retrieves task records needed for searching and filtering.               |
| `Feature/search/service.py`      | Applies search and filtering rules.                                      |
| `Feature/search/view.py`         | Provides the search, status, and priority controls.                      |
| `Feature/sort/`                  | Handles task sorting.                                                    |
| `Feature/sort/model.py`          | Contains sorting rules for deadline and priority.                        |
| `Feature/sort/repository.py`     | Provides task data for sorting-related operations.                       |
| `Feature/sort/service.py`        | Performs the sorting logic.                                              |
| `Feature/sort/view.py`           | Provides the sorting selection control.                                  |

---

## 7. Installation and Setup

### Requirements

* Python 3.10 or newer
* Tkinter
* SQLite

Tkinter and SQLite are normally included with Python.

### Step 1: Download or Clone the Repository

Clone the GitHub repository or download the project files.

### Step 2: Open the Project

Open the `FINAL_PROJECT_CS26L` folder using a code editor such as Visual Studio Code or another Python IDE.

### Step 3: Open a Terminal

Open a terminal inside the `FINAL_PROJECT_CS26L` folder.

### Step 4: Run the Application

Use:

```bash
python main.py
```

If your computer uses `python3`, use:

```bash
python3 main.py
```

### Database Setup

No manual database setup is required.

When the program starts, `Database.create_tables()` creates the `categories` and `tasks` tables if they do not already exist.

The database file is:

```text
database/tasks.db
```

---

## 8. How to Use the System

### Creating a Title

1. Open the application.
2. Click **New** under the Titles section.
3. Enter a title name.
4. Click the confirmation/save option.
5. The new title will appear in the title list.

### Adding a Task

1. Select a title.
2. Click **Add task**.
3. Enter the task name.
4. Select a deadline.
5. Select a priority.
6. Select a status.
7. Save the task.
8. The task will appear in the task table.

### Editing a Task

1. Select a task from the table.
2. Click **Edit task**.
3. Change the task information.
4. Save the changes.

### Deleting a Task

1. Select a task.
2. Click **Delete task**.
3. Confirm the deletion.

### Completing a Task

1. Select a task.
2. Click **Mark completed**.
3. The task status changes to `COMPLETED`.

### Searching for a Task

1. Use the **Search** field.
2. Enter part or all of the task name.
3. The task table updates automatically.

### Filtering Tasks

Use the:

* **Status** dropdown
* **Priority** dropdown

to display only tasks matching the selected filter.

### Sorting Tasks

Use **Sort by** and select:

* Added order
* Deadline
* Priority

---

## 9. OOP Implementation

The project uses classes to separate different responsibilities of the system.

### Important Classes

| Class                | Purpose                                                         |
| -------------------- | --------------------------------------------------------------- |
| `MainApp`            | Controls the main application window and connects the features. |
| `Database`           | Handles the SQLite database connection and table creation.      |
| `CategoryRepository` | Performs database operations for titles/categories.             |
| `CategoryService`    | Handles category business logic.                                |
| `TaskRepository`     | Performs database operations for tasks.                         |
| `TaskService`        | Handles task management operations.                             |
| `SearchCriteria`     | Stores search and filter information.                           |
| `SearchRepository`   | Retrieves task information for searching.                       |
| `SearchService`      | Performs search and filtering logic.                            |
| `SearchView`         | Provides the search and filter GUI.                             |
| `SortRule`           | Contains rules used for sorting tasks.                          |
| `SortRepository`     | Provides task data for the sorting feature.                     |
| `SortService`        | Performs task sorting.                                          |
| `SortView`           | Provides the sorting GUI.                                       |
| `ScrollDatePicker`   | Provides the month, day, and year selection interface.          |

### Encapsulation

Encapsulation is applied by separating data and operations into different classes.

For example, database SQL operations are handled by repository classes. The main GUI does not directly write SQL queries. Instead, it communicates with services such as `TaskService` and `CategoryService`.

The category service also validates title names before saving them.

### Inheritance

The project uses inheritance from Tkinter's `ttk.Frame`.

For example:

```python
class SearchView(ttk.Frame):
```

and:

```python
class SortView(ttk.Frame):
```

These classes inherit functionality from `ttk.Frame`.

The project does **not** have custom inheritance such as creating a child class from `Task`.

### Polymorphism

The project does not implement custom polymorphism between its own classes.

The system mainly uses separate services, repositories, and views for their specific responsibilities.

---

## 10. Database

The project uses **SQLite** as its database.

The database file is:

```text
database/tasks.db
```

The database contains two tables:

### Categories Table

| Column | Type    | Description                |
| ------ | ------- | -------------------------- |
| `id`   | INTEGER | Primary key                |
| `name` | TEXT    | Name of the title/category |

The category name is required and must be unique.

### Tasks Table

| Column        | Type    | Description                  |
| ------------- | ------- | ---------------------------- |
| `id`          | INTEGER | Primary key                  |
| `category_id` | INTEGER | Links the task to a category |
| `name`        | TEXT    | Task name                    |
| `deadline`    | TEXT    | Task deadline                |
| `priority`    | TEXT    | Task priority                |
| `status`      | TEXT    | Task status                  |

The `category_id` is a foreign key connected to the `categories` table.

```text
categories
    |
    | 1
    |
    | many
    ↓
tasks
```

Deleting a category also deletes its related tasks because the database uses `ON DELETE CASCADE`.

### Database Operations

#### Create

The system can create:

* New categories/titles
* New tasks

#### Read

The system can retrieve:

* All categories
* Individual tasks
* Task lists from the database

#### Update

The system can update:

* Category names
* Task names
* Task deadlines
* Task priorities
* Task statuses

#### Delete

The system can delete:

* Categories
* Tasks

When a category is deleted, its related tasks are also deleted.

#### Search and Filter

The search repository retrieves task information using a join between the `categories` and `tasks` tables.

The search service then filters the retrieved records based on:

* Keyword
* Status
* Priority
* Selected title

The search itself is therefore performed by the application logic after retrieving the records.

---

## 11. Screenshots

Add screenshots of the actual working application to this section.

### Screenshot 1 – Main Application

```text
[ <img width="1286" height="758" alt="image" src="https://github.com/user-attachments/assets/cba362cb-4ea0-4650-965e-8d7596dd39a3" />
 ]
```

**Description:** Shows the main Task Organizer and Tracker System window, including the Titles panel, search and filter controls, sorting control, task table, and task action buttons.

### Screenshot 2 – Add/Edit Task Window

```text
[ <img width="432" height="242" alt="image" src="https://github.com/user-attachments/assets/53e12385-5b93-4859-8416-a6c9b46cd662" />
 ]
```

**Description:** Shows the task form where the user can enter the task name, select a deadline, choose a priority, and choose a status.

### Screenshot 3 – Search and Filter

```text
[ <img width="673" height="82" alt="image" src="https://github.com/user-attachments/assets/302a1eb3-8ff8-4a62-8936-2e9aff73757c" />
 ]
```

**Description:** Shows the Search field and the Status and Priority filters being used to display specific tasks.

### Screenshot 4 – Sorting

```text
[ <img width="195" height="57" alt="image" src="https://github.com/user-attachments/assets/33350360-b521-45d4-9e2e-11e4502b8e20" />
 ]
```

**Description:** Shows the Sort by control with the available sorting options: Added order, Deadline, and Priority.

---

## 12. Testing

The project should be tested manually by running the application and checking each major feature.

| #  | Test                            | Expected Result                                                 | Actual Result      |
| -- | ------------------------------- | --------------------------------------------------------------- | ------------------ |
| 1  | Create a new title              | A new title appears in the Titles list.                         | Fill after testing |
| 2  | Create a duplicate title        | The system displays an error and does not create the duplicate. | Fill after testing |
| 3  | Add a valid task                | The task appears in the task table.                             | Fill after testing |
| 4  | Add a task with an empty name   | The system displays an error and does not save the task.        | Fill after testing |
| 5  | Add a task with a past deadline | The system displays an error and does not save the task.        | Fill after testing |
| 6  | Edit a task                     | The task information is updated.                                | Fill after testing |
| 7  | Delete a task                   | The selected task is removed.                                   | Fill after testing |
| 8  | Mark a task completed           | The task status changes to `COMPLETED`.                         | Fill after testing |
| 9  | Search for a task               | Matching task names are displayed.                              | Fill after testing |
| 10 | Filter by status                | Only tasks with the selected status are displayed.              | Fill after testing |
| 11 | Filter by priority              | Only tasks with the selected priority are displayed.            | Fill after testing |
| 12 | Sort by deadline                | Tasks are arranged according to their deadlines.                | Fill after testing |
| 13 | Sort by priority                | Tasks are arranged from HIGH to MEDIUM to LOW.                  | Fill after testing |
| 14 | Delete a title                  | The title and its related tasks are removed.                    | Fill after testing |

> **Important:** Replace `Fill after testing` with the actual result you observe when you run your submitted application. This avoids claiming that a test passed when there is no test record in the source code.

---

## 13. Known Issues / Limitations

The current implementation has the following limitations:

1. **No user login system**
   The application does not have user accounts or authentication.

2. **Local database only**
   The SQLite database is stored locally on the computer. It is not a shared online database.

3. **No cloud synchronization**
   Tasks cannot be synchronized between different computers.

4. **No automatic notifications**
   The system stores deadlines and allows sorting by deadline, but it does not provide a reminder notification when a deadline is reached.

5. **No task description field**
   Tasks currently store a task name, deadline, priority, and status.

6. **Manual testing**
   The project does not contain a dedicated automated testing framework.

7. **Sorting is handled in the application layer**
   The sorting service sorts the retrieved task records in Python rather than using an SQL `ORDER BY` query for the selected sorting option.

---

## 14. Author

**Name:** [Martin Roy P. Verdeflor]

**Section:** [3581]

---

