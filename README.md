# To-Do List Manager

A simple command-line To-Do List Manager built with Python. Manage your tasks by adding, displaying, completing, or deleting them, with all tasks stored persistently in a JSON file ('tasks.json').

## Features

- Add new tasks with a name
- Display all tasks with their completion status
- Mark tasks as completed
- Delete tasks
- Persistent storage in a pretty-printed JSON file

## Installation

1. Ensure you have **Python 3.13** or later from [python.org](https://www.python.org/).
2. Download the 'To-do_List_Manager.py' script.
3. Place the script in a directory where you have write permissions (for creating 'tasks.json').

## Usage

Run the script from the command line:

'''bash
python todo.py
'''

Follow the on-screen menu to manage your tasks. The menu provides options to:

- Add a task
- Display all tasks
- Mark a task as completed
- Delete a task
- Quit the program

### Example Interaction

'''
Task Manager Menu:
1: Add task
2: Display tasks
3: Complete task
4: Delete task
5: Quit
Enter your choice (1-5): 1
Enter the name of the task to add: Buy groceries
Task 'Buy groceries' added.

Task Manager Menu:
1: Add task
2: Display tasks
3: Complete task
4: Delete task
5: Quit
Enter your choice (1-5): 2
1. Task: Buy groceries, Status: Not Completed
'''

The tasks are saved in 'tasks.json', which is automatically created.

#### Example 'tasks.json' content:

'''json
[
  {
    "name": "Buy groceries",
    "completed": false
  }
]
'''

## File Structure

- 'todo.py': The main script to run the To-Do List Manager.
- 'tasks.json': Automatically created to store tasks in a pretty-printed JSON format.

## Troubleshooting

- **File Permission Errors**: Ensure the script has write access to the directory to create 'tasks.json'.
- **Invalid Inputs**: The program handles invalid inputs (e.g., non-numeric task numbers) gracefully and displays error messages like "Please enter a valid number."
- **Corrupted JSON File**: If 'tasks.json' is corrupted, the program starts with an empty task list.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository (if hosted on GitHub).
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a clear description of your changes.

Report issues or suggest features via the repository’s issue tracker.

## License
