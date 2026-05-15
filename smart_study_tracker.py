 import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
if os.path.exists(FILE_NAME):
with open(FILE_NAME, "r") as file:
return json.load(file)
return []

def save_tasks(tasks):
with open(FILE_NAME, "w") as file:
json.dump(tasks, file, indent=4)

def add_task(tasks):
title = input("Enter task title: ")
subject = input("Enter subject name: ")

task = {  
    "title": title,  
    "subject": subject,  
    "completed": False  
}  

tasks.append(task)  
save_tasks(tasks)  
print("\nTask added successfully!\n")

def view_tasks(tasks):
if not tasks:
print("\nNo tasks available.\n")
return

print("\nYour Tasks:\n")  

for index, task in enumerate(tasks, start=1):  
    status = "Completed" if task["completed"] else "Pending"  

    print(f"{index}. {task['title']}")  
    print(f"   Subject : {task['subject']}")  
    print(f"   Status  : {status}\n")

def complete_task(tasks):
view_tasks(tasks)

if not tasks:  
    return  

try:  
    task_number = int(input("Enter task number to mark completed: "))  

    if 1 <= task_number <= len(tasks):  
        tasks[task_number - 1]["completed"] = True  
        save_tasks(tasks)  
        print("\nTask marked as completed!\n")  
    else:  
        print("\nInvalid task number.\n")  

except ValueError:  
    print("\nPlease enter a valid number.\n")

def delete_task(tasks):
view_tasks(tasks)

if not tasks:  
    return  

try:  
    task_number = int(input("Enter task number to delete: "))  

    if 1 <= task_number <= len(tasks):  
        removed = tasks.pop(task_number - 1)  
        save_tasks(tasks)  
        print(f"\nDeleted task: {removed['title']}\n")  
    else:  
        print("\nInvalid task number.\n")  

except ValueError:  
    print("\nPlease enter a valid number.\n")

def main():
tasks = load_tasks()

while True:  
    print("=" * 40)  
    print(" SMART STUDY TRACKER ")  
    print("=" * 40)  
    print("1. Add Task")  
    print("2. View Tasks")  
    print("3. Mark Task Completed")  
    print("4. Delete Task")  
    print("5. Exit")  

    choice = input("\nEnter your choice: ")  

    if choice == "1":  
        add_task(tasks)  

    elif choice == "2":  
        view_tasks(tasks)  

    elif choice == "3":  
        complete_task(tasks)  

    elif choice == "4":  
        delete_task(tasks)  

    elif choice == "5":  
        print("\nThank you for using Smart Study Tracker!")  
        break  

    else:  
        print("\nInvalid choice. Try again.\n")

if name == "main":
main()