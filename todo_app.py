# Creating a very basic app for a todo list. 
# the goal is to create a simple todo list that can be managed by CLI. 
# Commands of adding, removing, tagging as completed, view list and close
import json
import os
from datetime import datetime
from InquirerPy import prompt
from cli_questions import *
from variables import tags, priority, status, new_tag, projects
from list_mgmt import *



# Relevant variables 
init = 0
current_project = ""

status = ['not started', 'on going', 'completed']
priority = ['low', 'medium', 'high']
tags = []

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

def load_data(project_name):
    file_name = project_name +".json"
    try:
        with open(file_name, "r") as file:
            tasks_data = json.load(file)
            tasks = [Task(**task_data) for task_data in tasks_data]
            # print(f"DEBUG: Loaded {len(tasks)} tasks from {file_name}")
            return tasks
    except FileNotFoundError:
        print(f"DEBUG: {file_name} not found, starting with an empty list.")
        return []
    except json.JSONDecodeError as e:
        # print(f"DEBUG: Error reading {file_name} - {e}, starting with an empty list.")
        return []

tasks = load_data(projects[0])

def add_task(desc, cat, stat, date, prio):
    tasks.append(Task(desc, cat, stat, date, prio))
    print("new item was added to list")

def view_list():
    i = 0
    if len(tasks)==0:
        print("your list is empty")
        return

    print(f'there are {len(tasks)} items in your list:')
    for task in tasks:
        print(f"  {i}. ({task.priority}): {task.description}")
        i = i+1

def save_data(project_name):
    file_name = project_name + ".json"
    
    data = [task.to_dict() for task in tasks ]

    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)
    # file.flush()
    # os.fsync(file.fileno())  # Ensure data is written to disk

    print(f"task saved successfully to {file_name}")

def remove_task(id):
    del tasks[id]
    os.system('cls')
    print(f'task {id} deleted')

def view_projects():
    i = 0
    if len(projects)==0:
        print("no projects found")
        return
    print(f'you have {len(projects)} projects listed:')
    for project in projects:
        print(f"{i}:\t {project}")
        i+=1
    

# Run App here  

# def main_menu():
#     print("\n \n")
#     result = first_prompt()

# def main_menu_short():
#     print("\n \n")
#     print("next command: ")

  

def run_app():
    global init
    
    view_projects()
    while True:
        print("\n =============================================================================")
        
        welcome_choice = welcome()
        result = welcome_choice['main_menu']

        if result == "a": # Open existing project
            name_temp = input('type project name: ')
            print(name_temp)
            name = name_temp["project_name"]
            print(name)
            save_data(name)
            tasks = load_data(name)
            projects.append(name)
            current_project = name
        elif result == "b": #create new project
            name_temp = new_project_view()
            print(name_temp)
            name = name_temp["project_name"]
            print(name)
            save_data(name)
            tasks = load_data(name)
            projects.append(name)
            current_project = name
        # elif result == "c": #create new project
        #     # do stuff
        # elif result == "d":
        #     # do stuff
        elif result == "e":
            break
        else:
            print('try again')
            
    





        temp_choice = list_main()
        choice = temp_choice['main_menu']
        print(choice)
        print("\n")
        # init = init + 1
        if choice == "1": ## Adding New Task
            results = new_task_info()
            add_task(results['task_description'], results['tags'], "not started", datetime.today().strftime("%c"), results['priority'])
            os.system('cls')
            print("task added to your list")
        elif choice == "2": ## Tagging as Completed
            id = int(input("select task id: "))
            tasks[id].status = "completed"
            os.system('cls')
            print(f"task {tasks[id].description} is now tagged as completed")
        elif choice == "3":  ## Deleting tasks      
            os.system('cls')
            view_list()
            id = input("select task id: ")
            if int(id) > len(tasks) -1:
                print("this id doesn't exit")
            else:
               remove_task(int(id))
               view_list()
        elif choice == "4": ## View list   
            os.system('cls')
            view_list()
        elif choice == "exit": ## Quit
            results = leaving()
            if results['save_task'] == True:
                save_data( "tasks.json")
            print("goodbye")
            break
        elif choice == "save":  ## Save
            os.system('cls')
            save_data("tasks.json")
        elif choice == "date": ## Today's date
            os.system('cls')
            print(f'{datetime.today().strftime("%c")}')
        elif choice == "tag": ## create new tag
            os.system('cls')
            results = new_tag_info()
            new_tag(results["tag_name"], results["tag_name"])
        else:
            print("invalid response. try again.")

if __name__ == "__main__":
    run_app()
