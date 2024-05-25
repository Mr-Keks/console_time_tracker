from ui.ui_handler import task_edit_menu_header

from ui.create_task_ui import CreateTaskUI


def update_task_name(task):
    # header
    section_header = task_edit_menu_header(task_name=task.get_task_name(), section="Edit task name")

    task.set_task_name(None)
    update_task_data(task, section_header)

def update_time_limited(task):
    # header
    section_header = task_edit_menu_header(task_name=task.get_task_name(), section="Edit time limited")

    type_of_stopwatch = "regular" if task.get_time_limited() else "time limited"

    section_header()
    user_seletion = input(f"Do you want switch to {type_of_stopwatch} stopwatch? (yes/no): ")

    if user_seletion == "yes": 
        task.set_time_limited(not task.get_time_limited)
    
    update_task_data(task, section_header)

def update_time_amount(task):
    # header
    section_header = task_edit_menu_header(task_name=task.get_task_name(), section="Edit time amount")
    
    task.set_amount_of_time(None)
    task.set_time_limited(None)
    update_task_data(task, section_header)

def update_start_position(task):
    # header
    section_header = task_edit_menu_header(task_name=task.get_task_name(), section="Edit start position")
    
    task.set_reverse_time(None)
    task.set_time_limited(None)
    update_task_data(task, section_header)

def back_to_task_menu(task):
    from ui.task_menu import task_menu_ui

    input("press any button to back task menu...")
    task_menu_ui(task.get_task_name())

def update_task_data(task, section_header):
    if task.get_time_limited() == None:
        if task.get_amount_of_time() and task.get_reverse_time():
            type_of_stopwatch = True
        else:
            type_of_stopwatch = False
    elif task.get_amount_of_time() is None or task.get_reverse_time() is None:
        type_of_stopwatch = False
    else:
        type_of_stopwatch = not task.get_time_limited()

    CreateTaskUI(
        header=section_header,
        task_name=task.get_task_name(),
        task_time_limited=task.get_time_limited(),
        task_amount_of_time=task.get_amount_of_time(),
        task_start_position=task.get_reverse_time(),
        type_of_stopwatch=type_of_stopwatch
    ).create_task_ui()

    back_to_task_menu(task)