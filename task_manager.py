
import csv
import datetime
import os
from typing import List, Dict, Optional

class TaskManager:
    def __init__(self, filename: str = "tasks.csv"):
        self.filename = filename
        self.tasks = []
        self.next_id = 1
        self.load_tasks()

    def load_tasks(self) -> None:
        """Load tasks from CSV file"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r', newline='', encoding='utf-8') as file:
                    reader = csv.DictReader(file)
                    self.tasks = list(reader)

                # Update next_id based on existing tasks
                if self.tasks:
                    max_id = max(int(task['task_id'][1:]) for task in self.tasks if task['task_id'].startswith('T'))
                    self.next_id = max_id + 1
            except Exception as e:
                print(f"Error loading tasks: {e}")
                self.tasks = []

    def save_tasks(self) -> None:
        """Save tasks to CSV file"""
        try:
            with open(self.filename, 'w', newline='', encoding='utf-8') as file:
                if self.tasks:
                    fieldnames = ['task_id', 'description', 'priority', 'status', 'date_created', 'date_completed']
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(self.tasks)
        except Exception as e:
            print(f"Error saving tasks: {e}")

    def add_task(self, description: str, priority: str = "Medium") -> str:
        """Add a new task"""
        task_id = f"T{self.next_id:03d}"
        task = {
            'task_id': task_id,
            'description': description,
            'priority': priority,
            'status': 'Pending',
            'date_created': datetime.date.today().strftime('%Y-%m-%d'),
            'date_completed': ''
        }
        self.tasks.append(task)
        self.next_id += 1
        self.save_tasks()
        return task_id

    def get_all_tasks(self) -> List[Dict]:
        """Get all tasks"""
        return self.tasks

    def get_pending_tasks(self) -> List[Dict]:
        """Get only pending tasks"""
        return [task for task in self.tasks if task['status'] == 'Pending']

    def get_completed_tasks(self) -> List[Dict]:
        """Get only completed tasks"""
        return [task for task in self.tasks if task['status'] == 'Completed']

    def mark_task_complete(self, task_id: str) -> bool:
        """Mark a task as completed"""
        for task in self.tasks:
            if task['task_id'] == task_id:
                task['status'] = 'Completed'
                task['date_completed'] = datetime.date.today().strftime('%Y-%m-%d')
                self.save_tasks()
                return True
        return False

    def delete_task(self, task_id: str) -> bool:
        """Delete a task"""
        for i, task in enumerate(self.tasks):
            if task['task_id'] == task_id:
                del self.tasks[i]
                self.save_tasks()
                return True
        return False

    def get_task_by_id(self, task_id: str) -> Optional[Dict]:
        """Get a specific task by ID"""
        for task in self.tasks:
            if task['task_id'] == task_id:
                return task
        return None

    def update_task(self, task_id: str, description: str = None, priority: str = None) -> bool:
        """Update task description or priority"""
        for task in self.tasks:
            if task['task_id'] == task_id:
                if description:
                    task['description'] = description
                if priority:
                    task['priority'] = priority
                self.save_tasks()
                return True
        return False

    def get_tasks_by_priority(self, priority: str) -> List[Dict]:
        """Get tasks filtered by priority"""
        return [task for task in self.tasks if task['priority'] == priority]