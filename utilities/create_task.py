from objects.task import Task
from utilities import save_data


def create_task(task_name, time_limited, amount_of_time, start_position):
    save = save_data.SaveTask(task_name=task_name)
    # initiation Task instance
    task = Task()

    # fill up task data
    task.set_task_name(task_name)

    if time_limited:
        task.set_amount_of_time(amount_of_time)
        if start_position:
            # stopwatch starts from the end
            task.set_reverse_time()
            task.set_task_destination(0)
            task.set_last_saved_time(int(task.get_amount_of_time()) * 60)
        else:
            # stopwatch start from the beginnig
            task.set_task_destination(int(task.get_amount_of_time()) * 60)
            task.set_last_saved_time(0)
    
    save.save_task(task)