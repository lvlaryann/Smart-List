# Smart List

A simple, chat-friendly Python to-do list app with persistent storage and task priorities. Great for learning, home projects, or as a starting point for your own productivity tools!

## Features
- Add, list, and mark to-do items as done
- Filter tasks by keyword
- Assign priorities to tasks (1 = most important)
- Persistent storage using SQLite (local only)
- Clean, readable Python code

## Usage
1. **Add a task:**
   ```python
   from src.main import add_todo
   add_todo('Buy groceries', priority=2)
   ```
2. **List tasks:**
   ```python
   from src.main import list_todos
   print(list_todos())
   ```
3. **Mark a task as done:**
   ```python
   from src.main import mark_done
   mark_done(1)  # where 1 is the task ID
   ```

## Project Structure
```
├── src/
│   ├── main.py         # Main app logic
│   └── __init__.py
├── tests/
│   ├── test_main.py    # Example test
│   └── __init__.py
├── .gitignore
├── LICENSE
├── README.md
```

## Local Database
- Your personal to-do items are stored in `todo.db` (excluded from GitHub by `.gitignore`).
- When sharing or publishing, your list remains private.

## Requirements
- Python 3.7+

## Running
You can run and test the app using the provided functions in `src/main.py`.

## License
MIT — see [LICENSE](LICENSE)

---
*Feel free to fork, star, or contribute!*
