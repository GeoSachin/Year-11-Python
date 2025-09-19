import json
import os

TODO_FILE = "todo_list.json"

# Load existing tasks or create an empty list
def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task(task):
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    print(f'Added: "{task}"')

# Remove a task
def remove_task(task_index):
    tasks = load_tasks()
    if 0 <= task_index < len(tasks):
        removed = tasks.pop(task_index)
        save_tasks(tasks)
        print(f'Removed: "{removed["task"]}"')
    else:
        print("Invalid task index.")

# Mark a task as done
def complete_task(task_index):
    tasks = load_tasks()
    if 0 <= task_index < len(tasks):
        tasks[task_index]["done"] = True
        save_tasks(tasks)
        print(f'Marked as done: "{tasks[task_index]["task"]}"')
    else:
        print("Invalid task index.")

# View all tasks
def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks yet!")
    else:
        for i, task in enumerate(tasks):
            status = "[✓]" if task["done"] else "[ ]"
            print(f'{i}. {status} {task["task"]}')

# Main loop
def main():
    while True:
        print("\nOptions: [add] [remove] [done] [view] [exit]")
        choice = input("Enter choice: ").strip().lower()
        
        if choice == "add":
            task = input("Enter new task: ").strip()
            add_task(task)
        elif choice == "remove":
            view_tasks()
            task_index = int(input("Enter task number to remove: "))
            remove_task(task_index)
        elif choice == "done":
            view_tasks()
            task_index = int(input("Enter task number to mark as done: "))
            complete_task(task_index)
        elif choice == "view":
            view_tasks()
        elif choice == "exit":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()