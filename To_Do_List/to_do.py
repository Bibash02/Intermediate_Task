import os
import json

FILE_NAME = 'to_do_list.json'

# load task from json file
def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, 'r') as file:
        return json.load(file)

# save tasj to json file
def save_tasks(tasks):
    with open(FILE_NAME, 'w') as file:
        json.dump(tasks, file, indent=4)

# generate unique task id
def generate_task_id(tasks):
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1

# Add a new task
def add_task(tasks):
    title = input("Enter a task title: ")
    task = {
        "id": generate_task_id(tasks),
        "title": title,
        "completed": False
    }
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")

# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    print("\n Your Tasks: ")
    for task in tasks:
        status = "Completed" if task["completed"] else "Pending"
        print(f"{task['id']}. {task['title']} | [{status}]")

def mark_task_completed(tasks):
    view_tasks(tasks)
    try:
        task_id = int(input("Enter the task ID to mark as completed: "))
        for task in tasks:
            if task["id"] == task_id:
                task["completed"] = True
                save_tasks(tasks)
                print("Task marked as completed!")
                return
        print("Task ID not found!")
    except ValueError:
        print("Invalid input! Please enter a valid task ID.")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_id = int(input("Enter the task ID to delete: "))
        for task in tasks:
            if task["id"] == task_id:
                tasks.remove(task)
                save_tasks(tasks)
                print("Task deleted successfully!")
                return
        print("Task ID not found!")
    except ValueError:
        print("Invalid input! Please enter a valid task ID.")

def main():
    tasks = load_tasks()

    while True:
        print("\n Welcom to the to-do list game")
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark task as completed")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_completed(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Exiting the to-do list game.")
            break
        else:
            print("Invalid choice! ")

if __name__ == "__main__":
    main()