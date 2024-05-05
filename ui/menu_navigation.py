import os

# ui functions
from objects.menu import Menu
from ui.ui_handler import clear_screen_and_print_title, check_range_of_option
from ui.create_task_ui import CreateTaskUI

# business logic
from utilities.create_task import create_task
from utilities.start_stopwatch import start_task

# files
from utilities import load_data

import time
import sys


# main menu section
def main_menu_ui():
    '''
        Main menu let user choose one of following options:
            1) create new task
            2) select one of exists task 
            3) close program
    '''

    # add header to the menu page
    clear_screen_and_print_title()
    Menu.main_menu() # print main menu

    menu_option = check_range_of_option(input("Select: "), 3)

    if not menu_option:
        print("Wrong option, press enter and try again!")
        input("press something back to main menu...")
        main_menu_ui()

    # create new task
    if menu_option == "1":
        CreateTaskUI().create_task_ui()
    # select exist tasks
    elif menu_option == "2":
        task_list_menu_ui()
    elif menu_option == "3":
        print("Thank you for using this program!")
        time.sleep(0.5)
        sys.exit(0)
    

def task_list_menu_ui():
    '''
        print list of created tasks
    '''
    clear_screen_and_print_title()

    tasks_list = load_data.check_tasks_list() # return list of exist tasks

    print("\nList of tasks:")
    for index, task in enumerate(tasks_list, start=1):
        print(f"{index}. {task}")

    task_index = check_range_of_option(input("Select your task: "), len(tasks_list))

    if task_index:
        task_menu_ui(tasks_list[int(task_index)-1])
    else:
        print('You entered invalid value!')
        input('press any button...')
        task_list_menu_ui()

# task menu 
def task_menu_ui(task_name):
    clear_screen_and_print_title()
    print("Task: ", task_name)
    Menu.task_menu()
    task_menu_selecter = check_range_of_option(input("Select: "), 2)

    if task_menu_selecter:
        if task_menu_selecter == "1":
            start_task_ui(task_name)
            input("press enter to back main menu...")
            main_menu_ui()
        elif task_menu_selecter == "2":
            main_menu_ui()
    else:
        input("You put wrong value!...")
        task_menu_ui(task_name)

# run stopwatch
def start_task_ui(task_name):
    print(f"\nTask: {task_name}")
    print("Press Enter to start the stopwatch...")
    input()
    print("Stopwatch started.")

    stopwatch = start_task(task_name)

    print("\nStopwatch stopped.")
    print(stopwatch)

    input("press enter to back main menu...")