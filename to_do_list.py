import json

def add_task():
    name = input("Task name: ")
    description = input("Task description: ")

    task = {"name": name, "description": description}
    return task

def delete_task():
    display_tasks(tasks)
    
    while True:
        num = input("enter a task number to delete: ")
        try:
            num = int(num)
            if num <= 0 or num > len(tasks):
                print("Invalid Number, out of range.")
            else:
                print("Task deleted")
                break
        except:
            print("Invalid Number")

    tasks.pop(num - 1)

def update_delete_task():
    while True:
        num = input("Enter the task number to update: ")
        try:
            num = int(num)
            if num <= 0 or num > len(tasks):
                print("Invalid Number, out of range.")
            else:
                break
        except:
            print("Invalid Number")

    tasks.pop(num - 1)
    

def update_add_task():
    name = input("Updated Task Name: ")
    description = input("Updated Task description: ")

    task = {"name": name, "description": description}
    return task


def display_tasks(tasks):
    for i, tasks in enumerate(tasks):
        print(i + 1, "-", tasks["name"])
        print("- Description:", tasks["description"])
        print("")

with open("tasks.json", "r") as f:
    tasks = json.load(f)["tasks"]

print("Hi, Welcome to your To Do List")
while True:
    print()
    if len(tasks) == 0:
        print("Your list has: 0 Tasks")
        print("Add more tasks in order to see them.")
    elif len(tasks) == 1:
        print("Your list has: 1 Task")
    else:
        print("Your list has: ", len(tasks), "Tasks")
    display_tasks(tasks)
    command = input("You can 'Add', 'Delete' or 'Update' a task, and 'Q' for quit: ").lower()
    if command == "add":
        task = add_task()
        tasks.append(task)
        display_tasks(tasks)
    elif command == "delete":
        delete_task()
        display_tasks(tasks)
    elif command == "update":
         update_delete_task()
         task = update_add_task()
         tasks.append(task)
         print("Task Updated")
    #this update works by deleting the task and adding a new one imeediately therefore giving the user the impression that it was updated
    elif command == "q":    
        break
    else:
        print("Invalid command")



with open("tasks.json", "w") as f:
    json.dump({"tasks": tasks}, f)