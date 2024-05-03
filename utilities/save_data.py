import json
import os

from datetime import datetime

from data.config import FOLDER_TASK_DATA_PATH, get_task_folder_path, get_task_file_path, get_log_task_file_path

class SaveTask:
	def __init__(self, task_name):
		self.task_folder_path = get_task_folder_path(task_name)
		self.task_file_path = get_task_file_path(task_name)
		self.task_log_file_path = get_log_task_file_path(task_name)

	def create_task_folder_and_files(self):
		try:
			if not os.path.exists(FOLDER_TASK_DATA_PATH):
				os.mkdir(FOLDER_TASK_DATA_PATH)
			# create folder
			os.mkdir(self.task_folder_path)
			# create empty task file
			with open(self.task_file_path, 'w') as file:
					json.dump({}, file)
		except Exception as e:
			print(e)
			input()

		# create empty log file
		with open(self.task_log_file_path, 'w') as file:
			json.dump({}, file)

	def save_task(self, task):
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
			# check if path exist
			if not os.path.exists(self.task_folder_path):
				# create task directory and files
				self.create_task_folder_and_files()

			# writing task data
			with open(self.task_file_path, "w") as file:
				json.dump(data_json, file, indent=4)

		except Exception as ex:
			print(ex)
			input()

	def save_task_log(self, task_time):
		'''
		saving spended time on task in task log file
		''' 

		# Attempt to open the file in read mode to load existing data
		current_day = datetime.now().date().isoformat()
		try:
			with open(self.task_log_file_path, "r") as file:
				log_task_data = json.load(file)
				# check if file already has current day record
				if current_day in log_task_data.keys():
					log_task_data[current_day]["spended_time"] += task_time
				else:
					# reuse already existed code
					raise FileNotFoundError

		# If the file doesn't exist or any other error occurs during file opening or JSON loading
		except (FileNotFoundError, json.decoder.JSONDecodeError):
			log_task_data = {
				current_day:  {"spended_time": task_time}  # Create new entry for the current day
			}
		# Write the updated or new data back to the file
		with open(self.task_log_file_path, "w") as file:
			json.dump(log_task_data, file, indent=4)