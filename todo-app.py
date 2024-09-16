# Creating a very basic app for a todo list. 
# the goal is to create a simple todo list that can be managed by CLI. 
# Commands of adding, removing, tagging as completed, view list and close


# Relevant variables 

class Task:
    def __init__(self, description, category, status, due_date, priority):
        self.description = description
        self.category = category
        self.status = status
        self.due_date = due_date
        self.priority = priority
    
    def display_task(self):
        print(f"{self.status} | Description: {self.description} \n Cat: {self.category} \n Due: {self.due_date} \n Priority: {self.priority}")

tasks = []


def add_task(desc, cat, stat, date, prio):
    tasks.append(Task(desc, cat, stat, date, prio))
    print("new item was added to list")

def view_list():
    i = 1
    if len(tasks)==0:
        print("list is empty")
        return
    print("################## \n All Tasks")
    for task in tasks:
        print(f"{i}. ({task.priority}): {task.description}")
        i = i+1


def main_menu():
    print("\n \n")
    print("welcome to Todo Manager!")
    print("select an option below:")
    print("1. add Task")
    print("2. tag as completed")
    print("3. remove Task")
    print("4. see All open Tasks")
    print("or type exit to leave the app")

def main_menu_short():
    print("\n \n")
    print("next command: ")

def run_app():
    while True:
        init = 0
        if init == 0:
            main_menu()
        else:
            main_menu_short()
        choice = input("enter your choice: ")
        init = init + 1

        if choice == "1":
            desc = input("task description: ")
            cat = input("category: ")
            date = input("due date: ")
            prio = input("priority (L/M/H): ")
            add_task(desc, cat, "not started", date, prio)
        elif choice == "2":
            id = input("select task id: ")
            tasks[id].status = "completed"
        elif choice == "3":
            print("not yet available")
        elif choice == "4":
            view_list()
        elif choice == "exit":
            print("goodbye")
            break
        else:
            print("invalid response. try again.")

if __name__ == "__main__":
    run_app()
