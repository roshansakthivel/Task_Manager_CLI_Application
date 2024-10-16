import json
from typing import List, Dict

class Task:
    def __init__(self, id: int, title: str, completed: bool = False):
        self.id = id
        self.title = title
        self.completed = completed

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "title": self.title,
            "completed": self.completed
        }

    @classmethod
    def from_dict(cls, data: Dict):
        return cls(data["id"], data["title"], data["completed"])

class TaskManager:
    def __init__(self):
        self.tasks: List[Task] = []
        self.load_tasks()

    def add_task(self, title: str):
        task_id = len(self.tasks) + 1
        new_task = Task(task_id, title)
        self.tasks.append(new_task)
        print(f"Task '{title}' added successfully with ID {task_id}.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        for task in self.tasks:
            status = "Completed" if task.completed else "Not Completed"
            print(f"ID: {task.id}, Title: {task.title}, Status: {status}")

    def delete_task(self, task_id: int):
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                print(f"Task with ID {task_id} deleted successfully.")
                return
        print(f"Task with ID {task_id} not found.")

    def complete_task(self, task_id: int):
        for task in self.tasks:
            if task.id == task_id:
                task.completed = True
                print(f"Task with ID {task_id} marked as completed.")
                return
        print(f"Task with ID {task_id} not found.")

    def save_tasks(self):
        with open("tasks.json", "w") as f:
            json.dump([task.to_dict() for task in self.tasks], f)
        print("Tasks saved successfully.")

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as f:
                task_data = json.load(f)
                self.tasks = [Task.from_dict(data) for data in task_data]
            print("Tasks loaded successfully.")
        except FileNotFoundError:
            print("No existing tasks file found. Starting with an empty task list.")

def main():
    task_manager = TaskManager()

    while True:
        print("\n--- Task Manager ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Complete")
        print("5. Save and Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter task title: ")
            task_manager.add_task(title)
        elif choice == "2":
            task_manager.view_tasks()
        elif choice == "3":
            task_id = int(input("Enter task ID to delete: "))
            task_manager.delete_task(task_id)
        elif choice == "4":
            task_id = int(input("Enter task ID to mark as complete: "))
            task_manager.complete_task(task_id)
        elif choice == "5":
            task_manager.save_tasks()
            print("Thank you for using Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()