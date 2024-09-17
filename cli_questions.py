from InquirerPy import prompt
from variables import tags_keypair, priority_keypair

def new_task_info():
    adding_task = [
        {
            "type": "input",
            "name": "task_description",
            "message": "Enter the task description:"
        },
        {
            "type": "list",
            "name": "tags",
            "message": "Select task tags:",
            "choices": tags_keypair
        },
        {
            "type": "input",
            "name": "duration",
            "message": "Estimated duration:",
            "validate": lambda result: result.isdigit() or "Please enter a valid number."
        },
        {
            "type": "list",
            "name": "priority",
            "message": "Select the task priority:",
            "choices": priority_keypair
        }
    ]
    answers = prompt(adding_task)
    return answers

            # desc = input("task description: ")
            # cat = input("category: ")
            # date = input("due date: ")
            # prio = input("priority (L/M/H): ")
            # add_task(desc, cat, "not started", date, prio)

def leaving():
    save = [
        {
        "type": "confirm",
        "name": "save_task",
        "message": "Do you want to save your progress?",
        "default": True,  # Default value is set to 'Yes'
        # "when": lambda result: result.get("1", False),

    }]
    answers = prompt(save)
    return answers

def first_prompt():
    menu = [
        {
            "type":"list",
            "name": "main_menu",
            "message":"Welcome to Thiago's todo manager App. Select one of the options below:",
            "choices":[
                {"name":"add new task", "value":"1"},
                {"name":"mark as completed", "value":"2"},
                {"name":"remove task", "value":"3"},
                {"name":"view all tasks", "value":"4"},
                {"name":"create new tag", "value":"tag"},
                {"name":"save progress", "value":"save"},
                {"name":"today's date", "value":"date"},
                {"name":"exit", "value":"exit"}
                
            ]
        }
    ]
    answers = prompt(menu)
    return answers
    
def new_tag_info():
    info = [
        {
            "type": "input",
            "name": "tag_name",
            "message": "tag name: "
        }

    ]
    answers = prompt(info)
    return answers
# template_questions = [
#     {
#         "type": "list",
#         "name": "priority",
#         "message": "Select the task priority:",
#         "choices": [
#             {"name": "High", "value": "High"},
#             {"name": "Medium", "value": "Medium"},
#             {"name": "Low", "value": "Low"}
#         ]
#     },
#     {
#         "type": "checkbox",
#         "name": "tags",
#         "message": "Select task tags:",
#         "choices": [
#             {"name": "Urgent", "value": "urgent"},
#             {"name": "Work", "value": "work"},
#             {"name": "Personal", "value": "personal"},
#             {"name": "Fitness", "value": "fitness"}
#         ]
#     },
#     {
#         "type": "input",
#         "name": "task_description",
#         "message": "Enter the task description:"
#     },
#     {
#         "type": "password",
#         "name": "password",
#         "message": "Enter your password:"
#     },
#     {
#         "type": "confirm",
#         "name": "confirm_task",
#         "message": "Do you want to add this task?",
#         "default": True  # Default value is set to 'Yes'
#     },
#     {
#         "type": "rawlist",
#         "name": "task_category",
#         "message": "Select a task category:",
#         "choices": [
#             {"name": "Work", "value": "work"},
#             {"name": "Personal", "value": "personal"},
#             {"name": "Fitness", "value": "fitness"}
#         ]
#     },
#     {
#         "type": "list",
#         "name": "secondary_category",  # Changed to avoid duplicate name keys
#         "message": "Select a category:",
#         "choices": [
#             {"name": "Work", "value": "Work"},
#             {"name": "Personal", "value": "Personal", "disabled": "Currently unavailable"},
#             {"name": "Fitness", "value": "Fitness"}
#         ]
#     },
#     {
#         "type": "input",
#         "name": "due_date",
#         "message": "Enter the task due date (YYYY-MM-DD):",
#         "validate": lambda result: True if len(result) == 10 else "Invalid date format. Use YYYY-MM-DD."
#     },
#     {
#         "type": "input",
#         "name": "age",
#         "message": "Enter your age:",
#         "validate": lambda result: result.isdigit() or "Please enter a valid number."
#     }
# ]

# answers = prompt(template_questions)
# print(f"Selected priority: {answers}")
