import json
import time
import threading
import os

from  datetime import datetime

from task import Task
from stopwatch import Stopwatch, listen_for_enter


FOLDER_DATA_NAME = "C:\\Users\\Mr Keks\\Desktop\\100_hours\\version 2\\tasks"

def save_task(task):
	data_json = {
		"task_name": task.get_task_name(),
		"time_limited": task.get_time_limited(),
		"amount_of_time": task.get_amount_of_time(),
		"reverse_time": task.get_reverse_time(),
		"last_saved_time": task.get_last_saved_time(),
		"task_destination": task.get_task_destination(),
		"zero_start": task.get_zero_start()
		}

	
	try: 
		task_folder_name = task.get_task_name()
		task_file_name = task.get_task_name()


		if not os.path.exists(f"{FOLDER_DATA_NAME}/{task_folder_name}"):
			# create task directory
			os.mkdir(f"{FOLDER_DATA_NAME}/{task_folder_name}")

		with open(f"{FOLDER_DATA_NAME}/{task_folder_name}/{task_file_name}.json", "w") as file:
			json.dump(data_json, file, indent=4)

	except Exception as ex:
		print(ex)
	

def save_task_log(task_name, task_time):
	'''
	saving spended time on task in task log file
	'''
	task_name = task_name  # Example task name
	task_time = task_time  # Example task time (replace with actual value)

	task_file_name = task_name
	task_folder_name = task_name
	log_task_data = {}

	current_day = datetime.now().date().isoformat()

	# Attempt to open the file in read mode to load existing data
	try: 
	    with open(f"{FOLDER_DATA_NAME}/{task_folder_name}/log_{task_file_name}.json", "r") as file:
	        log_task_data = json.load(file)
	        if current_day in log_task_data.keys():
	            log_task_data[current_day]["spended_time"] += task_time
	        else:
	            log_task_data[current_day] = {"spended_time": task_time}  # Create new entry for the current day

	# If the file doesn't exist or any other error occurs during file opening or JSON loading
	except (FileNotFoundError, json.decoder.JSONDecodeError):
	    log_task_data[current_day] = {"spended_time": task_time}  # Create new entry for the current day

	# Write the updated or new data back to the file
	with open(f"{FOLDER_DATA_NAME}/{task_folder_name}/log_{task_file_name}.json", "w") as file:
	    json.dump(log_task_data, file, indent=4)


def create_task():
	task = Task()

	task.set_task_name(input("Write your task name: "))
	if input("Do you want your task be time limited? (yes/no): ") == "yes":
		task.set_time_limited()

		task.set_amount_of_time(input("Set your time (minutes): "))

		if input("Do you prefer start your time from end? (yes/no): ") == "yes":
			task.set_reverse_time()
			task.set_task_destination(0)
			task.set_last_saved_time(int(task.get_amount_of_time()) * 60)
		else:
			task.set_task_destination(int(task.get_amount_of_time()) * 60)
			task.set_last_saved_time(0)
			
	else:
		task.set_last_saved_time(0)
		
	# check task information
	print("\n\nYour tasks info:")
	print(task.__str__())

	if input("Create new task? (yes/no): ") == "yes":
		save_task(task)
		
		print("\n\nYou successfuly created new file!")
	return task



def start_task(task):
	# create stopwatch instanse
	stopwatch = Stopwatch(
		start_time=task.get_last_saved_time(),
		stop_time=task.get_task_destination(),
		reverse=task.get_reverse_time(),
		zero_start=task.get_zero_start()
		)


	print(f"\nTask: {task.get_task_name()}")
	print("Press Enter to start the stopwatch...")
	input()

	enter_thread = threading.Thread(target=listen_for_enter, args=(stopwatch,))
	enter_thread.start()

	stopwatch.start()
	print("Stopwatch started.")

	stopwatch.display_time()
	enter_thread.join()

	print("\nStopwatch stopped.")
	print(stopwatch.display_compare_times())
	task.set_last_saved_time(stopwatch.last_updated_time)
	
	# saving task data
	save_task(task)
	print("task pass")
	save_task_log(task.get_task_name(), stopwatch.compare_times())
	print("log pass")

	input("press enter to back main menu...")

def check_tasks_list():
		try:
			tasks_file_name = []
			exists_data = os.listdir(FOLDER_DATA_NAME)
			if exists_data:
				for task_file_name in exists_data:
					tasks_file_name.append(task_file_name)
			
			if tasks_file_name:
				return tasks_file_name
			else:
				None
		except Exception as ex:
			print(ex)

def open_task_file(file_name):
	with open(f"{FOLDER_DATA_NAME}/{file_name}/{file_name}.json", "r") as file:
		data = json.load(file)
	task = Task(
		task_name=data["task_name"],
	    time_limited=data["time_limited"],
	    amount_of_time=data["amount_of_time"],
	    reverse_time=data["reverse_time"],
	    last_saved_time=data["last_saved_time"],
	    task_destination=data["task_destination"],
	    zero_start=data["zero_start"]
		) 

	return task

def open_task_log_file(file_name):
	try:
		with open(f"{FOLDER_DATA_NAME}/{file_name}/log_{file_name}.json", "r") as file:
			data = json.load(file)
			data = list(data.keys())

		return data[-1]
	# check if json is file empty 
	# it's true when task was created but stopwatch wasn't run before
	except (FileNotFoundError, json.decoder.JSONDecodeError):
		return True

def check_reset_stopwatch(task, log_last_date):
	if datetime.now().date().isoformat() == log_last_date:
		task.set_zero_start(False)
	else:
		task.set_zero_start(True) 