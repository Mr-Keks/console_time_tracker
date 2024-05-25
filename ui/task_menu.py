from ui.ui_handler import check_range_of_option, task_menu_header

from objects.menu import Menu

from utilities.load_data import LoadTask
from utilities.update_task import update_start_position, update_task_name, update_time_amount, update_time_limited


def select_option(list_range):
    return check_range_of_option(input("\nSelect: "), list_range)

def back_to_main_menu():
    from ui.menu_navigation import main_menu_ui
    main_menu_ui()

def back_to_task_list():
    from ui.menu_navigation import task_list_menu_ui
    task_list_menu_ui()

# task info menu
def show_task_info(task, task_name):
    task_menu_header(task_name)
    Menu.task_menu_show_info(task.__str__())

    menu_selecter = check_range_of_option(input("\nSelect: "), 2)
    
    if menu_selecter:
        if menu_selecter == "1":
            edit_task(task)
        elif menu_selecter == "2":
            task_menu_ui(task_name)
    else: 
        print("You selected unavaliable value!")
        input("press...")
        show_task_info(task, task_name)

# edit task

def edit_task(task):
    task_menu_header(task.get_task_name())
    Menu.task_edit_menu(task.get_time_limited())
    list_range = 5 if task.get_time_limited() else 3
    edit_menu_selecter = select_option(list_range)

    # update task name
    if edit_menu_selecter == '1':
        update_task_name(task)
    # update time limited
    elif edit_menu_selecter == '2':
        update_time_limited(task)
    if task.get_time_limited():
        # update time amount
        if edit_menu_selecter == '3':
            update_time_amount(task)
        # update start position
        elif edit_menu_selecter == '4':
            update_start_position(task)
    # back to task menu
    if edit_menu_selecter == '5' or edit_menu_selecter == '3':
        task_menu_ui(task.get_task_name())
    


# task main menu
def task_menu_ui(task_name):
    task_menu_header(task_name)
    Menu.task_menu()
    task = LoadTask(task_name).open_task_file()
    task_menu_selecter = check_range_of_option(input("\nSelect: "), 5)

    if task_menu_selecter:
        # start stopwatch
        if task_menu_selecter == "1":
            from ui.menu_navigation import start_task_ui

            start_task_ui(task_name)
            input("\npress enter to back main menu...")
            back_to_main_menu()
        # show task info
        elif task_menu_selecter == "2":
            show_task_info(task, task_name)
        # edit task
        elif task_menu_selecter == "3":
            edit_task(task)
        # back to task list
        elif task_menu_selecter == "4":
            back_to_task_list()
        # back to main menu
        elif task_menu_selecter == "5":
            back_to_main_menu()
    else:
        input("You put wrong value!...")
        task_menu_ui(task_name)