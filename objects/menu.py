class Menu:
	'''
	menu
	'''

	def main_menu():
		print("\tMain Menu\n\n")
		print("1. Create new task")
		print("2. Select task")
		print("3. Exit")

	def task_menu():
		print("\n\tTask Menu\n\n")
		print("1. Start stopwatch")
		print("2. Show task info")
		print("3. Edit task")
		print("4. Back to main menu")
	
	def task_menu_show_info(task_info):
		print("\n\tTask Info\n\n")
		print(task_info)
		print("\n1. Edit task")
		print("2. Back to task menu")
