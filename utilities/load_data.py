import json
import os

from data.config import FOLDER_TASK_DATA_PATH, get_task_folder_path, get_task_file_path, get_log_task_file_path, get_ui_for_create_task
from objects.task import Task

class LoadTask:
    def __init__(self, task_name):
        self.task_folder_path = get_task_folder_path(task_name)
        self.task_file_path = get_task_file_path(task_name)
        self.task_log_file_path = get_log_task_file_path(task_name)
	
    def open_task_file(self):
        with open(self.task_file_path, "r") as file:
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
    
    def open_task_log_file(self):
        try:
            with open(self.task_log_file_path) as file:
                data = json.load(file)
                data = list(data.keys())

            # return last record day
            return data[-1]
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            pass
        except IndexError:
            return None

def check_tasks_list():
    '''
        This function check '/tasks/' folder from 'data'
        and return list of folders that are exsisting tasks
    '''
    try:
        tasks_file_name = []
        print(FOLDER_TASK_DATA_PATH)
        exists_data = os.listdir(FOLDER_TASK_DATA_PATH)
        if exists_data:
            for task_file_name in exists_data:
                tasks_file_name.append(task_file_name)
        
        if tasks_file_name:
            return tasks_file_name
        else:
            None
    except Exception as ex:
        pass

def load_create_task_text_data():
    '''
        load text ui information for create_task_ui
        method
    '''
    text_data_dump_folder = get_ui_for_create_task()
    with open(text_data_dump_folder / "create_task.json", "r") as file:
        data = json.load(file)

    return data