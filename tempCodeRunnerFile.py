import json


try:
    with open("data.json", "r") as file:
        tasks = json.load(file)
except FileNotFoundError:
    tasks = []


def show_tasks():
        print("To-do List:")
        for Index, task in enumerate(tasks, start=1):
            status = "✓" if task["done"] else "✗"
            print(f"{Index}: [{status}] {task['name']}")
            
def add_task():
        task_name = input("enter the task: ")
        tasks.append({"name": task_name, "done": False})

def mark_done():
        show_tasks()
        done_task = int(input("which task has been done: "))
        tasks[done_task-1]["done"]=True

def delete_task():
        show_tasks()
        del_task = int(input("Which task would u like to delete: "))
        tasks.pop(del_task-1)

def store_tasks():
        with open("data.json", "w") as file:
              json.dump(tasks, file)

def view_tasks():
        with open("data.json", "r") as file:
              return json.load(file)
while True:

 
    user_input = int(input(''' 
        1. Add task
        2. View tasks
        3. Mark task as done 
        4. Delete Task
        5. Quit
        '''))
    
    if user_input == 1:
        add_task()
        store_tasks()
    elif user_input == 2:
        tasks = view_tasks()
        show_tasks()
    elif user_input == 3:
        mark_done()
        store_tasks()
    elif user_input == 4:
        delete_task()
        store_tasks()
    else:
        break