import os

from pathlib import Path

FOLDER_TASK_DATA_PATH = Path(__file__).resolve().parent
FOLDER_TASK_DATA_PATH = FOLDER_TASK_DATA_PATH / 'tasks'

def get_task_folder_path(folder_name):
    return FOLDER_TASK_DATA_PATH / folder_name

def get_task_file_path(file_name):
    folder_path = get_task_folder_path(file_name)
    return folder_path / (file_name + '.json')

def get_log_task_file_path(file_name):
    folder_path = get_task_folder_path(file_name)
    return folder_path / ('log_' + file_name + '.json')

