class Menu:
	'''
	menu
	'''

	def main_menu():
		print("\tMain Menu\n\n")
		print("1. Create new task")
		print("2. Select task")
		print("3. Exit")

	# kind of task menu
	def task_menu():
		print("\n\tTask Menu\n\n")
		print("1. Start stopwatch")
		print("2. Show task info")
		print("3. Edit task")
		print("4. Back to task list")
		print("5. Back to main menu")
	
	def task_menu_show_info(task_info):
		print("\n\tTask Info\n\n")
		print(task_info)
		print("\n1. Edit task")
		print("2. Back to task menu")
	
	def task_edit_menu(time_limited):
		print("\n\tEdit Task\n\n")
		print("1. Change 'task name'")
		print("2. Change 'time limited'")
		if time_limited:
			print("3. Change 'time amount'")
			print("4. Change 'start position'")
			print("5. Back to task menu")
		else:
			print("3. Back to task menu")


