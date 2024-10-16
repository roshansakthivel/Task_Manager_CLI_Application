# Task_Manager_CLI_Application

A simple command-line interface (CLI) application to manage tasks. This application allows users to add, view, delete, and mark tasks as complete. Tasks are saved to and loaded from a JSON file.

## Features

- Add new tasks
- View all tasks with their completion status
- Delete tasks by ID
- Mark tasks as complete
- Save tasks to a file (tasks.json)
- Load tasks from a file when the application starts

## How to Run

1. Ensure you have Python 3.6 or later installed on your system.
2. Clone or download this repository to your local machine.
3. Open a terminal or command prompt and navigate to the project directory.
4. Run the following command:

   ```
   python task_manager.py
   ```

5. Follow the on-screen prompts to interact with the Task Manager.

## Usage

The application presents a menu with the following options:

1. Add Task: Enter a task title to add a new task.
2. View Tasks: Display all tasks with their IDs, titles, and completion status.
3. Delete Task: Enter a task ID to remove it from the list.
4. Mark Task as Complete: Enter a task ID to mark it as completed.
5. Save and Exit: Save all tasks to the file and exit the application.

## File Storage

Tasks are automatically loaded from `tasks.json` when the application starts (if the file exists). When you choose to save and exit, all current tasks are saved to `tasks.json` in the same directory as the script.

## Development

This project is written in Python and uses the built-in `json` module for file handling. The code is structured into two main classes:

- `Task`: Represents individual tasks with ID, title, and completion status.
- `TaskManager`: Handles all task management operations and file I/O.


## How OUTPUT works(Working Process with EXAMPLE) -- 
--- Task Manager ---
 1. Add Task
2. View Tasks
3. Delete Task
4. Mark Task as Complete
5. Save and Exit
Enter your choice (1-5): 1
Enter task title: Demo Task 1

--- Task Manager ---
1. Add Task
2. View Tasks
3. Delete Task
4. Mark Task as Complete
5. Save and Exit
Enter your choice (1-5): 2
ID: 1, Title: Demo Task 1, Status: Not Completed

--- Task Manager ---
Enter your choice (1-5): 4
Enter the task ID to mark as complete: 1
Task marked as completed.

--- Task Manager ---
Enter your choice (1-5): 2
ID: 1, Title: Demo Task 1, Status: Completed

--- Task Manager ---
Enter your choice (1-5): 5
Tasks saved successfully.
Thank you for using Task Manager. Goodbye!


  




  
