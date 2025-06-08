import sqlite3
import os
import re

DB_FILE = os.path.join(os.path.dirname(__file__), '..', 'todo.db')

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    # Add priority column if it doesn't exist
    c.execute('''CREATE TABLE IF NOT EXISTS todos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL,
        done INTEGER DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        priority INTEGER DEFAULT 3
    )''')
    # Try to add priority column if missing (for upgrades)
    try:
        c.execute('ALTER TABLE todos ADD COLUMN priority INTEGER DEFAULT 3')
    except sqlite3.OperationalError:
        pass  # Already exists
    conn.commit()
    conn.close()

def add_todo(task, priority=3):
    init_db()
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('INSERT INTO todos (task, priority) VALUES (?, ?)', (task, priority))
    conn.commit()
    conn.close()
    return f"Added: '{task}' (priority {priority})"

def list_todos(criteria=None):
    init_db()
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('SELECT id, task, done, priority FROM todos ORDER BY priority ASC, created_at ASC')
    rows = c.fetchall()
    conn.close()
    if not rows:
        return "No to-do items found."
    filtered = rows
    if criteria:
        filtered = [row for row in rows if re.search(criteria, row[1], re.IGNORECASE)]
        if not filtered:
            return f"No to-do items found matching '{criteria}'."
    result = []
    for row in filtered:
        status = '✓' if row[2] else ' '
        result.append(f"[{row[0]}] [{status}] (P{row[3]}) {row[1]}")
    return '\n'.join(result)

def mark_done(todo_id):
    init_db()
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('UPDATE todos SET done = 1 WHERE id = ?', (todo_id,))
    conn.commit()
    conn.close()
    return f"Marked item {todo_id} as done."

# Usage in chat:
# - To add: add_todo('your task', priority=1)
# - To list: list_todos() or list_todos('keyword')
# - To mark done: mark_done(id)

if __name__ == "__main__":
    print("This module is now designed for chat-based interaction. Use the functions add_todo, list_todos, and mark_done from the chat window.")
