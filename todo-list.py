import json
import os

FILE_NAME = "tasks.json"


def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def show_tasks(tasks):
    if not tasks:
        print("\n✅ Your list is empty!")
    else:
        print("\n--- YOUR TO-DO LIST ---")
        for i, task in enumerate(tasks, 1):
            status = "✔" if task["done"] else " "
            print(f"{i}. [{status}] {task['title']}")


def main():
    tasks = load_tasks()

    while True:
        show_tasks(tasks)
        print("\nOptions: (1) Add (2) Done (3) Remove (4) Exit")
        choice = input("Select an option: ")

        if choice == "1":
            title = input("Enter task: ")
            tasks.append({"title": title, "done": False})
        elif choice == "2":
            num = int(input("Task number to mark done: ")) - 1
            if 0 <= num < len(tasks):
                tasks[num]["done"] = True
        elif choice == "3":
            num = int(input("Task number to remove: ")) - 1
            if 0 <= num < len(tasks):
                tasks.pop(num)
        elif choice == "4":
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
