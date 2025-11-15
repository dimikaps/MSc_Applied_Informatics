from datetime import datetime
import re  # Regular Expression module for data validation 


def add_new_task():
    task = {
    "Registration Date": None,
    "Task ID": None,
    "Task Description": None,
    "Assignee": None,
    "Phone Number": None,
    "Deadline": None
    }

    for key in task.keys(): 
        if key == "Registration Date":
            registration_date = datetime.now()
            registration_date_str = registration_date.strftime("%Y-%m-%d")
            task["Registration Date"] = registration_date_str
        elif key == "Task ID":
            global task_id  # I used global, in order to access the global task_id
            task_id += 1
            task["Task ID"] = task_id
        elif key == "Task Description":
            task[key] = input(f"Type the {key}: ")
        elif key == "Assignee":
            pattern = r"^[A-Za-z ]+$"
            while True:
                user_input = input(f"Type the {key}: ").capitalize()
                if re.match(pattern, user_input):
                    task[key] = user_input
                    break
                else:
                    print("Your input is not valid.")
        elif key == "Phone Number":
            pattern = r"^[0-9 ]+$"
            while True:
                user_input = input(f"Type the {key}: ").strip()
                if re.match(pattern, user_input):
                    task[key] = user_input
                    break
                else:
                    print("Your input is not valid.")
        elif key == "Deadline":
            pattern = r"^20[0-9]{2}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$"
            while True:
                user_input = input(f"Type the {key} (YYYY-MM-DD): ")
                if re.match(pattern, user_input):
                    task[key] = user_input
                    break
                else:
                    print("Your input is not valid.")
                     
    task_list.append(task)


def edit_task():
    while True:
        try:
            requested_task_id = int(input("Type the Task ID to locate the task you want to edit: "))
            break
        except ValueError as e:
            print("Task ID not Valid")
    for task in task_list:
        if task["Task ID"] == requested_task_id:
            print("Task Found")
            requested_key = input("Type the key you want to edit (Task Description/Assignee/Phone Number/Deadline): ")
            task[requested_key] = input(f"Modify the {requested_key}: ")


def delete_task():
    requested_task_id = int(input("Type the Task ID to locate the task you want to delete: "))
    found = False  # I initialize a variable to False to check if the requested task id exists. If it doesn't exist, stays False and prints a corresponding message
    for i, task in enumerate(task_list):  # Enumerate funtion gives index to each object which is very usefull for locating/deleting
        if task["Task ID"] == requested_task_id:
            del task_list[i]
            found = True
            break  # Stop looping once the item is deleted
    if found:
        print("Delete Successful")
    else:
        print("Requested Task ID doesn't exist, try again.")


def preview_tasks():
    for task in task_list:
        print(task)


def search_by_assignee():
    requested_assignee = input("Type the name of the Assignee for a task: ")
    non_existing_value = True
    for task in task_list:
        if task["Assignee"] == requested_assignee:
            print(task)
            non_existing_value = False
    if non_existing_value:
        print("Requested Assignee doesn't exist, try again.")


def search_by_date():
    requested_registration_date = input("Type the date of the task registration (YYYY-MM-DD): ")
    non_existing_value = True
    for task in task_list:
        if task["Registration Date"] == requested_registration_date:
            print(task)
            non_existing_value = False
    if non_existing_value:
        print("Requested Registration Date doesn't exist, try again.")


def preview_sorted_assignees_with_task_countity():
    task_counter_by_assignee.clear()  # Reset dictionary to recalculate counts after edits    
    for task in task_list:
        if task["Assignee"] in task_counter_by_assignee:
            task_counter_by_assignee[task["Assignee"]] += 1
            task_counter_list.append(task_counter_by_assignee)
        else:
            task_counter_by_assignee[task["Assignee"]] = 1
            task_counter_list.append(task_counter_by_assignee)
    print(task_counter_by_assignee)


def search_for_the_busiest_assignee():
    task_counter_by_assignee.clear()  # Reset dictionary to recalculate counts after edits
    for task in task_list:
        if task["Assignee"] in task_counter_by_assignee:
            task_counter_by_assignee[task["Assignee"]] += 1
            task_counter_list.append(task_counter_by_assignee)
        else:
            task_counter_by_assignee[task["Assignee"]] = 1
        task_counter_list.append(task_counter_by_assignee)
    print(task_counter_by_assignee)
    max_value = 0
    assignee_with_max_tasks = None
    for assignee, task_quantity in task_counter_by_assignee.items():
        if task_quantity > max_value:
            max_value = task_quantity
            assignee_with_max_tasks = assignee
    print(f"The busiest person is {assignee_with_max_tasks}")


def exit_programm():
    global running
    running = False


task_list = [
    {
        "Registration Date": "2025-11-03",
        "Task ID": 1,
        "Task Description": "Fix server issue",
        "Assignee": "Maria",
        "Phone Number": "6974219053",
        "Deadline": "2025-11-18"
    },
    {
        "Registration Date": "2025-11-06",
        "Task ID": 2,
        "Task Description": "Prepare report",
        "Assignee": "Alex",
        "Phone Number": "6982334478",
        "Deadline": "2025-11-20"
    },
    {
        "Registration Date": "2025-11-08",
        "Task ID": 3,
        "Task Description": "Update website",
        "Assignee": "Eleni",
        "Phone Number": "6945123209",
        "Deadline": "2025-11-22"
    },
    {
        "Registration Date": "2025-11-04",
        "Task ID": 4,
        "Task Description": "Client meeting",
        "Assignee": "George",
        "Phone Number": "6992348765",
        "Deadline": "2025-11-16"
    },
    {
        "Registration Date": "2025-11-10",
        "Task ID": 5,
        "Task Description": "Refactor code",
        "Assignee": "Chris",
        "Phone Number": "6968432190",
        "Deadline": "2025-11-25"
    },
    {
        "Registration Date": "2025-11-07",
        "Task ID": 6,
        "Task Description": "Write documentation",
        "Assignee": "Nikos",
        "Phone Number": "6938451290",
        "Deadline": "2025-11-19"
    },
    {
        "Registration Date": "2025-11-02",
        "Task ID": 7,
        "Task Description": "Email follow-up",
        "Assignee": "Dimitris",
        "Phone Number": "6956123400",
        "Deadline": "2025-11-15"
    },
    {
        "Registration Date": "2025-11-11",
        "Task ID": 8,
        "Task Description": "Security check",
        "Assignee": "Anna",
        "Phone Number": "6978901234",
        "Deadline": "2025-11-27"
    },
    {
        "Registration Date": "2025-11-05",
        "Task ID": 9,
        "Task Description": "Database backup",
        "Assignee": "Dimitris",
        "Phone Number": "6994321890",
        "Deadline": "2025-11-21"
    },
    {
        "Registration Date": "2025-11-09",
        "Task ID": 10,
        "Task Description": "Test new feature",
        "Assignee": "John",
        "Phone Number": "6947852134",
        "Deadline": "2025-11-24"
    }
]

task_id = 10  # I start by 10 because we already have 10 tasks

task_counter_by_assignee = {}

task_counter_list = []

running = True

while running:

    print("\nWelcome to Task Manager app 1.0:\n"
        "Press the corresponding number to what you want to do\n"
        "1. Add New Task\n"
        "2. Edit Task\n"
        "3. Delete Task\n"
        "4. Preview Tasks\n"
        "5. Search by Assignee\n"
        "6. Search by Date\n"
        "7. Preview sorted Assignees with task countity\n"
        "8. Search for the busiest Assignee\n"
        "0. Exit Programm")

    try:
        user_option = int(input("What to you want to do: ").strip())
        if user_option < 0 or user_option > 8:  # I choose to raise ValueError if the user enters an option which has no valid
            raise ValueError
    except ValueError as e:
        print("Option not valid, try again!", e)
        continue  # I use to continue because without it, it will enter the main program even with wrong input

    if user_option == 1:
        add_new_task()

    elif user_option == 2:
        edit_task()

    elif user_option == 3:
        delete_task()

    elif user_option == 4:
        preview_tasks()

    elif user_option == 5:
        search_by_assignee()

    elif user_option == 6:
        search_by_date()

    elif user_option == 7:
        preview_sorted_assignees_with_task_countity()

    elif user_option == 8:
        search_for_the_busiest_assignee()

    elif user_option == 0:
        exit_programm()
