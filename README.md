# Personal To-Do List Manager

A simple command-line interface (CLI) application for managing daily tasks built with Python.

## Features

- ✅ Add new tasks with priority levels
- 📋 View all tasks, pending tasks, or completed tasks
- ✏️ Update existing tasks
- ✅ Mark tasks as completed
- 🗑️ Delete tasks
- 🔍 Filter tasks by priority
- 📊 View task statistics
- 💾 Automatic data persistence using CSV files

## Installation

1. Make sure you have Python 3.6+ installed
2. Clone or download the project files
3. No additional dependencies required (uses only standard Python libraries)

## Usage

Run the application:
```bash
python main.py
```

### Main Menu Options

1. **Add new task** - Create a new task with description and priority
2. **View all tasks** - Display all tasks in a formatted table
3. **View pending tasks** - Show only incomplete tasks
4. **View completed tasks** - Show only finished tasks
5. **Mark task as complete** - Update task status to completed
6. **Update task** - Modify task description or priority
7. **Delete task** - Remove a task permanently
8. **Filter tasks by priority** - View tasks by High/Medium/Low priority
9. **Task statistics** - View completion rates and priority breakdown
0. **Exit** - Save and quit the application

## File Structure

```
Personal-to-do-list-cli/
├── main.py           # Main application entry point
├── task_manager.py   # Core task management logic
├── tasks.csv         # Data storage file (auto-generated)
└── README.md         # This file
```

## Data Storage

Tasks are automatically saved to `tasks.csv` with the following structure:
- `task_id`: Unique identifier (T001, T002, etc.)
- `description`: Task description
- `priority`: High, Medium, or Low
- `status`: Pending or Completed
- `date_created`: Creation date (YYYY-MM-DD)
- `date_completed`: Completion date (YYYY-MM-DD or empty)

## Sample Data

The application comes with sample tasks to demonstrate functionality:
- Data analytics assignments
- Personal errands
- Professional tasks
- Various priority levels

## Error Handling

- Input validation for priorities and task IDs
- File I/O error handling
- Graceful handling of invalid menu choices
- Confirmation prompts for destructive operations

## Requirements

- Python 3.6 or higher
- No external dependencies

## License

This project is for educational purposes as part of a data analytics course.
