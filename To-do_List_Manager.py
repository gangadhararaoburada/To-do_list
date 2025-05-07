'''Develop a simple to-do list application using Python with an emphasis on functions and data structures.'''

import json
import sys

# Ensure Python 3.13 or later
if sys.version_info <= (3, 13):
    print("Error: This code requires Python 3.13 or later.")
    sys.exit(1)

# Print Python version and compatibility status
print(f"Running on Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
print("This version is compatible and supported.")
    
# Function to load tasks from a JSON file
def load_tasks(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Function to save tasks to a JSON file
def save_tasks(tasks, filename):
    with open(filename, 'w') as f:
        json.dump(tasks, f, indent=2)

# Define the filename for persistence
filename = 'tasks.json'

# Load tasks from the file at startup
tasks = load_tasks(filename)

# Function to add a task
def add_task(task_name):
    if task_name.strip():
        tasks.append({"name": task_name, "completed": False})
        save_tasks(tasks, filename)
        print(f"Task '{task_name}' added.")
    else:
        print("Task name cannot be empty.")

# Function to delete a task
def delete_task(task_number):
    if 1 <= task_number <= len(tasks):
        task_name = tasks[task_number - 1]["name"]
        del tasks[task_number - 1]
        save_tasks(tasks, filename)
        print(f"Task '{task_name}' deleted.")
    else:
        print("Invalid task number.")

# Function to display all tasks
def display_tasks():
    if not tasks:
        print("No tasks to display.")
    else:
        for i, task in enumerate(tasks, start=1):
            status = "Completed" if task["completed"] else "Not Completed"
            print(f"{i}. Task: {task['name']}, Status: {status}")

# Function to mark a task as complete
def complete_task(task_number):
    if 1 <= task_number <= len(tasks):
        task_name = tasks[task_number - 1]["name"]
        tasks[task_number - 1]["completed"] = True
        save_tasks(tasks, filename)
        print(f"Task '{task_name}' marked as complete.")
    else:
        print("Invalid task number.")

# Main function to handle user input
def handle_user_input():
    while True:
        print("\nTask Manager Menu:")
        print("1: Add task")
        print("2: Display tasks")
        print("3: Complete task")
        print("4: Delete task")
        print("5: Quit")
        user_choice = input("Enter your choice (1-5): ")
        
        if user_choice == '1':
            task_name = input("Enter the name of the task to add: ")
            add_task(task_name)
        elif user_choice == '2':
            display_tasks()
        elif user_choice == '3':
            try:
                task_number = int(input("Enter the number of the task to mark as complete: "))
                complete_task(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif user_choice == '4':
            try:
                task_number = int(input("Enter the number of the task to delete: "))
                delete_task(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif user_choice == '5':
            print("Thank you for using Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Start the task management system
handle_user_input()
