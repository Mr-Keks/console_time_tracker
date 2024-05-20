from ui.ui_handler import clear_screen_and_print_title, check_range_of_option

from objects.menu import Menu

from utilities.load_data import LoadTask


def back_to_main_menu():
    from ui.menu_navigation import main_menu_ui
    main_menu_ui()

def back_to_task_list():
    from ui.menu_navigation import task_list_menu_ui
    task_list_menu_ui()

def print_task_menu_header(task_name):
    clear_screen_and_print_title()
    print("\t\t\t Task: ", task_name, "\n")

# task info menu
def show_task_info(task, task_name):
    print_task_menu_header(task_name)
    Menu.task_menu_show_info(task.__str__())

    menu_selecter = check_range_of_option(input("\nSelect: "), 2)
    
    if menu_selecter:
        if menu_selecter == "1":
            pass
        elif menu_selecter == "2":
            task_menu_ui(task_name)
    else: 
        print("You selected unavaliable value!")
        input("press...")
        show_task_info(task, task_name)


# task main menu
def task_menu_ui(task_name):
    print_task_menu_header(task_name)
    Menu.task_menu()
    task = LoadTask(task_name).open_task_file()
    task_menu_selecter = check_range_of_option(input("\nSelect: "), 4)

    if task_menu_selecter:
        # start stopwatch
        if task_menu_selecter == "1":
            from ui.menu_navigation import start_task_ui

            start_task_ui(task_name)
            input("press enter to back main menu...")
            back_to_main_menu()
        # show task info
        elif task_menu_selecter == "2":
            show_task_info(task, task_name)
        # edit task
        elif task_menu_selecter == "3":
            pass
        # back to task list
        elif task_menu_selecter == "4":
            back_to_task_list()
        # back to main menu
        elif task_menu_selecter == "5":
            back_to_main_menu()
    else:
        input("You put wrong value!...")
        task_menu_ui(task_name)