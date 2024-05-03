import os

# ui functions
from objects.menu import Menu
from ui.ui_handler import clear_screen_and_print_title

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

    menu_option = input("Select: ")

    # create new task
    if menu_option == "1":
        create_task_ui()
    # select exist tasks
    elif menu_option == "2":
        task_list_menu_ui()
    elif menu_option == "3":
        print("Thank you for using this program!")
        time.sleep(1)
        sys.exit(0)
    else:
        print("Wrong option, press enter and try again")
        input()


# create task menu
def create_task_ui():
    clear_screen_and_print_title()
    print("\tTask creation menu\n")
    # default properties
    task_amount_of_time=None
    task_start_positon=None

    task_name = input("Enter your task name: ")
    type_of_stopwatch = input("What kind of stopwatch you want create?\n\t1) regular\n\t2) time limited ")
    # task_time_limited = input("Do you want your task be time limited? (yes/no): ")
    
    # time limited stopwatch
    if type_of_stopwatch == "2":
        task_time_limited = True
        task_amount_of_time = input("Set your time (minutes): ")
        task_start_positon = input("Do you prefer start your time from end? (yes/no): ")
        task_start_positon = True if task_start_positon == 'yes' else False
    # regular stopwatch
    elif type_of_stopwatch == "1":
        task_time_limited = False
    else: 
        input("Wrong value!\nPlease select proper option! ...")
        create_task_ui()
    # check task information
    print("\n\nYour tasks info:\n")
    print('Task name: ', task_name)
    print('Task limited: ', task_time_limited)
    if task_time_limited == "yes":
        print('Amount of lime: ', task_amount_of_time)
        print('Task start postion: {}'.format(
            task_amount_of_time+':00' if task_start_positon else '00:00'))

    if input("Create new task? (yes/no): ") == "yes":
        create_task(
            task_name=task_name,
            time_limited=task_time_limited,
            amount_of_time=task_amount_of_time,
            start_position=task_start_positon
        )
        
        print("\n\nYou successfuly created new file!")
    main_menu_ui()

# task list menu

def task_list_menu_ui():
    clear_screen_and_print_title()

    tasks_list = load_data.check_tasks_list() # return list of exist tasks

    print("\nList of tasks:")
    for index, task in enumerate(tasks_list, start=1):
        print(f"{index}. {task}")

    task_index = input("Select your task: ")
    task_menu_ui(tasks_list[int(task_index)-1])

# task menu 
def task_menu_ui(task_index):
    clear_screen_and_print_title()
    Menu.task_menu()
    task_menu_selecter = input("Select: ")

    if task_menu_selecter == "1":
        start_task_ui(task_index)
        input("press enter to back main menu...")
        main_menu_ui()
    elif task_menu_selecter == "2":
        main_menu_ui()
    else:
        input("You put wrong value!...")
        task_menu_ui()

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