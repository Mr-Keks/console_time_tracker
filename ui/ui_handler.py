import os

def clear_screen_and_print_title():
    os.system("cls")
    print("\t\t\t Task time tracker \n\n")

def print_task_menu_header(task_name):
    clear_screen_and_print_title()
    print("\t\t\t Task: ", task_name, "\n")

def check_range_of_option(input_value, options_range):
    '''
        function generate range of list values
        and check if user input value in this range
    '''
    options_range = [str(option) for option in range(options_range+1)]
    
    if input_value in options_range:
        return input_value
    else:
        return False