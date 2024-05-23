from ui.ui_handler import print_task_menu_header


def update_task_name(task):
    # header
    print_task_menu_header(task.get_task_name())
    print("Edit task name\n")

    # body
    new_task_name = input("Please, enter new task name: ")
    try:
        task.set_task_name(new_task_name)
        print("You successful updated ")
        back_to_task_menu(task)
    except Exception as ex:
        print(ex)

def update_time_limited(task):
    # header
    print_task_menu_header(task.get_task_name())
    print("Edit time limited\n")

    task_limited = task.get_time_limited()

    if task_limited:
        user_selection = input("Do you want disable time limited option? (yes/no): ")
    else:
        user_selection = input("Do you want to active lime limited option? (yes/no): ")
    
    if user_selection == "yes":
        task.set_time_limited()
    else:
        input("press any button to back to main menu...")
    back_to_task_menu(task)

def update_time_amount(task):
    # header
    print_task_menu_header(task.get_task_name())
    print("Edit time amount\n")

    try:
        new_time = int(input("Please, enter new time amount: "))
        task.set_amount_of_time(new_time)
    except TypeError:
        print("You have put digit value!")
        input("Press to try again...")
        update_time_amount(task)

def update_start_position(task):
    # header
    print_task_menu_header(task.get_task_name())
    print("Edit start position")

    start_position = task.get_zero_start()

    if start_position:
        user_selection = input("Do you want start stopwatch from the end? (yes/no): " )
    else:
        user_selection = input("Do you want start stopwatch from the beginning? (yes/no): " )
    
    if user_selection == "yes":
        task.set_zero_start()
    else:
        input("press any button back to main menu...")
        back_to_task_menu(task)

def back_to_task_menu(task):
    from ui.task_menu import task_menu_ui

    input("press any button to back task menu...")
    task_menu_ui(task.get_task_name())