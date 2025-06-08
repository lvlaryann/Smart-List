import unittest
from src.main import add_todo, list_todos, mark_done
import os
import re

class TestToDoList(unittest.TestCase):
    def setUp(self):
        # Use a separate test database
        self.test_db = os.path.join(os.path.dirname(__file__), '..', 'test_todo.db')
        from src import main
        main.DB_FILE = self.test_db
        # Clean up the test db before each test
        if os.path.exists(self.test_db):
            os.remove(self.test_db)

    def tearDown(self):
        if os.path.exists(self.test_db):
            os.remove(self.test_db)

    def test_add_and_list_todo(self):
        add_todo('Test task', priority=2)
        result = list_todos()
        self.assertIn('Test task', result)
        self.assertIn('(P2)', result)

    def test_mark_done(self):
        add_todo('Another task', priority=1)
        # Get the id of the task
        result = list_todos('Another task')
        match = re.search(r'\[(\d+)\]', result)
        self.assertIsNotNone(match)
        todo_id = int(match.group(1))
        mark_done(todo_id)
        result_after = list_todos('Another task')
        self.assertIn('✓', result_after)

    def test_filter_todos(self):
        add_todo('Paint the fence', priority=3)
        add_todo('Fix the roof', priority=1)
        filtered = list_todos('paint')
        self.assertIn('Paint the fence', filtered)
        self.assertNotIn('Fix the roof', filtered)

if __name__ == "__main__":
    unittest.main()
