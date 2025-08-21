
import unittest
import os
from task_manager import TaskManager

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.test_filename = "test_tasks.csv"
        self.task_manager = TaskManager(self.test_filename)

    def tearDown(self):
        """Clean up after each test method."""
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def test_add_task(self):
        """Test adding a new task"""
        task_id = self.task_manager.add_task("Test task", "High")
        self.assertEqual(task_id, "T001")
        self.assertEqual(len(self.task_manager.tasks), 1)

    def test_mark_task_complete(self):
        """Test marking a task as complete"""
        task_id = self.task_manager.add_task("Test task", "Medium")
        result = self.task_manager.mark_task_complete(task_id)
        self.assertTrue(result)

        task = self.task_manager.get_task_by_id(task_id)
        self.assertEqual(task['status'], 'Completed')

    def test_delete_task(self):
        """Test deleting a task"""
        task_id = self.task_manager.add_task("Test task", "Low")
        result = self.task_manager.delete_task(task_id)
        self.assertTrue(result)
        self.assertEqual(len(self.task_manager.tasks), 0)

    def test_get_pending_tasks(self):
        """Test getting pending tasks"""
        self.task_manager.add_task("Pending task", "High")
        task_id = self.task_manager.add_task("To complete", "Medium")
        self.task_manager.mark_task_complete(task_id)

        pending_tasks = self.task_manager.get_pending_tasks()
        self.assertEqual(len(pending_tasks), 1)
        self.assertEqual(pending_tasks[0]['description'], "Pending task")

if __name__ == '__main__':
    unittest.main()
