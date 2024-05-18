from objects.task import Task
from utilities import save_data
from utilities.validation import str_time_format, int_time_format


def create_task(task_name, time_limited, amount_of_time, start_position):
    save = save_data.SaveTask(task_name=task_name)
    # initiation Task instance
    task = Task()

    # fill up task data
    task.set_task_name(task_name)
    task.set_time_limited(time_limited)

    if time_limited:
        task.set_amount_of_time(str_time_format(amount_of_time))
        if start_position:
            # stopwatch starts from the end
            task.set_reverse_time()
            task.set_task_destination(0)
            task.set_last_saved_time(int_time_format(amount_of_time))
        else:
            # stopwatch start from the begining
            task.set_task_destination(int_time_format(amount_of_time))
            task.set_last_saved_time(0)
    
    save.save_task(task)