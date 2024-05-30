import os
from bluffpaddingcypher.cypher import encrypt, decrypt

TODO_FILE = "tasks.txt"
ENCRYPTION_KEY = "your-secret-key"  # Replace with your actual encryption key

def load_tasks():
    tasks = []
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            lines = file.readlines()
            for line in lines:
                decrypted_task = decrypt(line.strip())
                tasks.append(decrypted_task)
    return tasks

def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        for task in tasks:
            encrypted_task = encrypt(task)
            file.write(encrypted_task + "\n")

def display_menu():
    print("\n" + "="*40)
    print("            TO-DO LIST MENU")
    print("="*40)
    print("1. Add Task")
    print("2. Update Task")
    print("3. Delete Task")
    print("4. Clear All Tasks")
    print("5. Exit")
    print("="*40)
    print("Enter your choice: ", end="")

def add_task(tasks):
    task = input("\nEnter the new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("\nTask added.")

def update_task(tasks):
    display_tasks(tasks)
    if tasks:
        try:
            task_id = int(input("\nEnter the task number to update: ")) - 1
            if 0 <= task_id < len(tasks):
                new_task = input("\nEnter the updated task: ")
                tasks[task_id] = new_task
                save_tasks(tasks)
                print("\nTask updated.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def delete_task(tasks):
    display_tasks(tasks)
    if tasks:
        try:
            task_id = int(input("\nEnter the task number to delete: ")) - 1
            if 0 <= task_id < len(tasks):
                tasks.pop(task_id)
                save_tasks(tasks)
                print("\nTask deleted.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def clear_all_tasks(tasks):
    confirm = input("\nAre you sure you want to clear all tasks? (y/n): ")
    if confirm.lower() == 'y':
        tasks.clear()
        save_tasks(tasks)
        print("\nAll tasks cleared.")

def display_tasks(tasks):
    if not tasks:
        print("\nNo tasks in the list.")
    else:
        print("\nCurrent Tasks:")
        print("="*40)
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
        print("="*40)

def main():
    tasks = load_tasks()
    
    while True:
        display_menu()
        choice = input().strip()

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            update_task(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            clear_all_tasks(tasks)
        elif choice == '5':
            print("\nExiting the to-do list program.")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 5.")

        display_tasks(tasks)

if __name__ == "__main__":
    main()
