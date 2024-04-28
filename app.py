import os

from app_engine import create_task, start_task, check_tasks_list, open_task_file, check_reset_stopwatch, open_task_log_file
from menu import Menu


menu = Menu()

while True:
	os.system("cls")
	print("\t\t\t Task time tracker \n\n\n")
	menu.main_menu()

	menu_option = input("Select: ")

	if menu_option == "1":
		create_task()
	elif menu_option == "2":
		tasks_list = check_tasks_list()

		print("\nList of tasks:")
		for index, task in enumerate(tasks_list, start=1):
			print(f"{index}. {task}")

		task_selecter = input("Select your task: ")
		task = open_task_file(tasks_list[int(task_selecter)-1])
		task_log = open_task_log_file(tasks_list[int(task_selecter)-1])
		check_reset_stopwatch(task, task_log)

		os.system("cls")
		print("\t\t\t Task time tracker \n\n\n")
		menu.task_menu()

		task_menu_selecter = input("Select: ")

		if task_menu_selecter == "1":
			task_result = start_task(task)


	elif menu_option == "3":
		break
		print("Thank you for using this program!")
		time.sleep(1)
		sys.exit(0)
	else:
		print("Wrong option, press enter and try again")
		input()
