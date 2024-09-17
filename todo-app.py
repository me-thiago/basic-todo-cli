# Creating a very basic app for a todo list. 
# the goal is to create a simple todo list that can be managed by CLI. 
# Commands of adding, removing, tagging as completed, view list and close
import json
from datetime import datetime
from InquirerPy import prompt
from cli_questions import *



# Relevant variables 
init = 0



class Task:
    def __init__(self, description, category, status, due_date, priority):
        self.description = description
        self.category = category
        self.status = status
        self.due_date = due_date
        self.priority = priority
    
    def display_task(self):
        print(f"{self.status} | Description: {self.description} \n Cat: {self.category} \n Due: {self.due_date} \n Priority: {self.priority}")

    def to_dict(self):
        return {
            "description": self.description,
            "category": self.category,
            "status": self.status,
            "due_date": self.due_date,
            "priority": self.priority
        }
    
    def __repr__(self):
        return f"Task(description={self.description}, category={self.category}, status={self.status}, due_date={self.due_date}, priority={self.priority})"

def load_data(file_name="tasks.json"):
    try:
        with open(file_name, "r") as file:
            tasks_data = json.load(file)
            tasks = [Task(**task_data) for task_data in tasks_data]
            # print(f"DEBUG: Loaded {len(tasks)} tasks from {file_name}")
            return tasks
    except FileNotFoundError:
        # print(f"DEBUG: {file_name} not found, starting with an empty list.")
        return []
    except json.JSONDecodeError as e:
        # print(f"DEBUG: Error reading {file_name} - {e}, starting with an empty list.")
        return []
tasks = load_data("tasks.json")

def add_task(desc, cat, stat, date, prio):
    tasks.append(Task(desc, cat, stat, date, prio))
    print("new item was added to list")

def view_list():
    i = 1
    if len(tasks)==0:
        print("your list is empty")
        return

    print(f'there are {len(tasks)} items in your list:')
    for task in tasks:
        print(f"  {i}. ({task.priority}): {task.description}")
        i = i+1

def save_data(tasks, file_name="tasks.json"):
    try:
        with open(file_name, "r") as file:
            data =json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
    
    data = [task.to_dict() for task in tasks ]

    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)
    print(f"task saved successfully to {file_name}")


    

# Run App here  

# def main_menu():
#     print("\n \n")
#     result = first_prompt()

# def main_menu_short():
#     print("\n \n")
#     print("next command: ")

  

def run_app():
    global init

    tasks = load_data("tasks.json")

    # Debugging: Print the tasks list after loading
    # print(f"DEBUG: Initial tasks list after loading: {tasks}")
    print("\n")
    view_list()
    while True:
        # if init == 0:
        #     main_menu()
        # else:
        #     main_menu_short()
        
        # init += 1
        print("\n =============================================================================")
        temp_choice = first_prompt()
        choice = temp_choice['main_menu']
        print(choice)
        print("\n")
        # init = init + 1
        if choice == "1":
            results = new_task_info()
            desc = results['task_description']
            cat = results['tags']
            print(f"the results are {results['duration']}")
            duration = datetime.strptime(results['duration'], '%d').date()
            print(duration)
            date = datetime.today()
            prio = results['priority']
            # desc = input("task description: ")
            # cat = input("category: ")
            # date = input("due date: ")
            # prio = input("priority (L/M/H): ")
            add_task(desc, cat, "not started", date, prio)
        elif choice == "2":
            id = input("select task id: ")
            tasks[id].status = "completed"
        elif choice == "3":
            print("not yet available")
        elif choice == "4":
            view_list()
        elif choice == "exit":
            results = leaving()
            if results['save_task'] == True:
                save_data(tasks, "tasks.json")
            print("goodbye")
            break
        elif choice == "save":
            save_data(tasks, "tasks.json")
        elif choice == "date":
            print(f'{datetime.today().strftime("%c")}')
        else:
            print("invalid response. try again.")

if __name__ == "__main__":
    run_app()
