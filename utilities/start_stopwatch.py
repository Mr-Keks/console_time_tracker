from objects.stopwatch import Stopwatch, listen_for_enter
from objects.task import Task

from utilities import load_data
from utilities import save_data

from datetime import datetime

import threading

def check_reset_stopwatch(task, log_last_date):
	if datetime.now().date().isoformat() == log_last_date:
		task.set_zero_start(False)
	else:
		task.set_zero_start(True) 

def start_task(task_name):
	task = Task()
	load = load_data.LoadTask(task_name=task_name)
	task = load.open_task_file()
	task_log = load.open_task_log_file()
	if task_log:
		check_reset_stopwatch(task, task_log)

	# create stopwatch instanse
	stopwatch = Stopwatch(
		start_time=task.get_last_saved_time(),
		stop_time=task.get_task_destination(),
		reverse=task.get_reverse_time(),
		zero_start=task.get_zero_start()
		)

	enter_thread = threading.Thread(target=listen_for_enter, args=(stopwatch,))
	enter_thread.start()

	stopwatch.start()

	stopwatch.display_time()
	enter_thread.join()

	task.set_last_saved_time(stopwatch.last_updated_time)

	# saving task data
	saving = save_data.SaveTask(task_name)
	saving.save_task(task)
	saving.save_task_log(stopwatch.compare_times())

	return stopwatch.display_compare_times()

	