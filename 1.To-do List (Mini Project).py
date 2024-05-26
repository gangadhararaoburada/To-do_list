'''Develop a simple to-do list application using Python with an emphasis on functions and data structures.'''

# Initialize an empty list to store the tasks
tasks = []

# Function to add a task
def add_task(task_name):
    tasks.append({"name": task_name, "completed": False})

# Function to delete a task
def delete_task(task_number):
    if task_number - 1 < len(tasks):
        del tasks[task_number - 1]

# Function to display the list of tasks
def display_tasks():
    for i, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Not Completed"
        print(f"{i}. Task: {task['name']}, Status: {status}")

# Function to mark a task as complete
def complete_task(task_number):
    if task_number - 1 < len(tasks):
        tasks[task_number - 1]["completed"] = True

# Function to handle user input
def handle_user_input():
    while True:
        print("\n1: Add task\n2: Delete task\n3: Display tasks\n4: Complete task\n5: Quit")
        user_choice = input("Enter your choice: ")
        
        if user_choice == '1':
            task_name = input("Enter the name of the task to add: ")
            add_task(task_name)
        elif user_choice == '2':
            task_number = int(input("Enter the number of the task to delete: "))
            delete_task(task_number)
        elif user_choice == '3':
            display_tasks()
        elif user_choice == '4':
            task_number = int(input("Enter the number of the task to mark as complete: "))
            complete_task(task_number)
        elif user_choice == '5':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Call the function to handle user input
handle_user_input()
