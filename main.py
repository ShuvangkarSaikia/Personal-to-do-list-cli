
from task_manager import TaskManager
import sys

class TodoApp:
    def __init__(self):
        self.task_manager = TaskManager()

    def display_menu(self):
        """Display the main menu"""
        print("\n" + "="*50)
        print("     PERSONAL TO-DO LIST MANAGER")
        print("="*50)
        print("1. Add new task")
        print("2. View all tasks")
        print("3. View pending tasks")
        print("4. View completed tasks")
        print("5. Mark task as complete")
        print("6. Update task")
        print("7. Delete task")
        print("8. Filter tasks by priority")
        print("9. Task statistics")
        print("0. Exit")
        print("-"*50)

    def display_tasks(self, tasks, title="Tasks"):
        """Display tasks in a formatted table"""
        if not tasks:
            print(f"\nNo {title.lower()} found.")
            return

        print(f"\n{title}:")
        print("-"*80)
        print(f"{'ID':<6} {'Description':<25} {'Priority':<10} {'Status':<12} {'Created':<12}")
        print("-"*80)

        for task in tasks:
            description = task['description'][:22] + "..." if len(task['description']) > 25 else task['description']
            print(f"{task['task_id']:<6} {description:<25} {task['priority']:<10} {task['status']:<12} {task['date_created']:<12}")
        print("-"*80)

    def get_valid_priority(self):
        """Get valid priority input from user"""
        while True:
            priority = input("Enter priority (High/Medium/Low) [default: Medium]: ").strip()
            if not priority:
                return "Medium"
            if priority.title() in ["High", "Medium", "Low"]:
                return priority.title()
            print("Invalid priority. Please enter High, Medium, or Low.")

    def add_task(self):
        """Add a new task"""
        print("\n--- Add New Task ---")
        description = input("Enter task description: ").strip()
        if not description:
            print("Task description cannot be empty!")
            return

        priority = self.get_valid_priority()
        task_id = self.task_manager.add_task(description, priority)
        print(f"✓ Task added successfully! ID: {task_id}")

    def view_all_tasks(self):
        """View all tasks"""
        tasks = self.task_manager.get_all_tasks()
        self.display_tasks(tasks, "All Tasks")

    def view_pending_tasks(self):
        """View pending tasks"""
        tasks = self.task_manager.get_pending_tasks()
        self.display_tasks(tasks, "Pending Tasks")

    def view_completed_tasks(self):
        """View completed tasks"""
        tasks = self.task_manager.get_completed_tasks()
        self.display_tasks(tasks, "Completed Tasks")

    def mark_task_complete(self):
        """Mark a task as complete"""
        print("\n--- Mark Task as Complete ---")
        pending_tasks = self.task_manager.get_pending_tasks()
        if not pending_tasks:
            print("No pending tasks to complete.")
            return

        self.display_tasks(pending_tasks, "Pending Tasks")
        task_id = input("\nEnter task ID to mark as complete: ").strip().upper()

        if self.task_manager.mark_task_complete(task_id):
            print(f"✓ Task {task_id} marked as complete!")
        else:
            print("Task not found or already completed.")

    def update_task(self):
        """Update a task"""
        print("\n--- Update Task ---")
        tasks = self.task_manager.get_all_tasks()
        if not tasks:
            print("No tasks available to update.")
            return

        self.display_tasks(tasks)
        task_id = input("\nEnter task ID to update: ").strip().upper()

        task = self.task_manager.get_task_by_id(task_id)
        if not task:
            print("Task not found.")
            return

        print(f"\nCurrent task: {task['description']}")
        print(f"Current priority: {task['priority']}")

        new_description = input("Enter new description (press Enter to keep current): ").strip()
        new_priority = input("Enter new priority (High/Medium/Low, press Enter to keep current): ").strip()

        if new_priority and new_priority.title() not in ["High", "Medium", "Low"]:
            print("Invalid priority. Update cancelled.")
            return

        if new_priority:
            new_priority = new_priority.title()

        if self.task_manager.update_task(task_id, new_description or None, new_priority or None):
            print(f"✓ Task {task_id} updated successfully!")
        else:
            print("Failed to update task.")

    def delete_task(self):
        """Delete a task"""
        print("\n--- Delete Task ---")
        tasks = self.task_manager.get_all_tasks()
        if not tasks:
            print("No tasks available to delete.")
            return

        self.display_tasks(tasks)
        task_id = input("\nEnter task ID to delete: ").strip().upper()

        confirm = input(f"Are you sure you want to delete task {task_id}? (y/N): ").strip().lower()
        if confirm == 'y':
            if self.task_manager.delete_task(task_id):
                print(f"✓ Task {task_id} deleted successfully!")
            else:
                print("Task not found.")
        else:
            print("Delete cancelled.")

    def filter_by_priority(self):
        """Filter tasks by priority"""
        print("\n--- Filter by Priority ---")
        priority = self.get_valid_priority()
        tasks = self.task_manager.get_tasks_by_priority(priority)
        self.display_tasks(tasks, f"{priority} Priority Tasks")

    def show_statistics(self):
        """Show task statistics"""
        all_tasks = self.task_manager.get_all_tasks()
        pending_tasks = self.task_manager.get_pending_tasks()
        completed_tasks = self.task_manager.get_completed_tasks()

        print("\n--- Task Statistics ---")
        print(f"Total tasks: {len(all_tasks)}")
        print(f"Pending tasks: {len(pending_tasks)}")
        print(f"Completed tasks: {len(completed_tasks)}")

        if all_tasks:
            completion_rate = (len(completed_tasks) / len(all_tasks)) * 100
            print(f"Completion rate: {completion_rate:.1f}%")

        # Priority breakdown
        high_priority = len([t for t in all_tasks if t['priority'] == 'High'])
        medium_priority = len([t for t in all_tasks if t['priority'] == 'Medium'])
        low_priority = len([t for t in all_tasks if t['priority'] == 'Low'])

        print(f"\nPriority breakdown:")
        print(f"High priority: {high_priority}")
        print(f"Medium priority: {medium_priority}")
        print(f"Low priority: {low_priority}")

    def run(self):
        """Main application loop"""
        print("Welcome to Personal To-Do List Manager!")

        while True:
            self.display_menu()
            choice = input("Enter your choice (0-9): ").strip()

            try:
                if choice == '1':
                    self.add_task()
                elif choice == '2':
                    self.view_all_tasks()
                elif choice == '3':
                    self.view_pending_tasks()
                elif choice == '4':
                    self.view_completed_tasks()
                elif choice == '5':
                    self.mark_task_complete()
                elif choice == '6':
                    self.update_task()
                elif choice == '7':
                    self.delete_task()
                elif choice == '8':
                    self.filter_by_priority()
                elif choice == '9':
                    self.show_statistics()
                elif choice == '0':
                    print("\nThank you for using Personal To-Do List Manager!")
                    print("Your tasks have been saved automatically.")
                    sys.exit(0)
                else:
                    print("Invalid choice. Please enter a number between 0-9.")

            except KeyboardInterrupt:
                print("\n\nExiting application...")
                sys.exit(0)
            except Exception as e:
                print(f"An error occurred: {e}")

            input("\nPress Enter to continue...")

if __name__ == "__main__":
    app = TodoApp()
    app.run()
