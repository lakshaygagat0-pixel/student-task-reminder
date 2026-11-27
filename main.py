from datetime import datetime

tasks = []


def add_task():
    title = input("Enter task name: ").strip()
    if not title:
        print("Task name cannot be empty.")
        return

    due_date = input("Enter due date (YYYY-MM-DD): ").strip()

    try:
        datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format.")
        return

    tasks.append({
        "title": title,
        "due_date": due_date,
        "completed": False
    })
    print("Task added successfully!")


def view_tasks():
    if not tasks:
        print("No tasks available.")
        return

    print("\n--- YOUR TASKS ---")
    for index, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{index}. {task['title']} | Due: {task['due_date']} | {status}")


def complete_task():
    view_tasks()
    if not tasks:
        return

    try:
        number = int(input("Enter task number to complete: "))
        if 1 <= number <= len(tasks):
            tasks[number - 1]["completed"] = True
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    while True:
        print("\n===== STUDENT TASK REMINDER =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()