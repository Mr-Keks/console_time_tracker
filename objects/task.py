class Task:
	'''
	task
	'''
	def __init__(self, 
			  task_name=None, 
			  time_limited=False,
			  amount_of_time=None, 
			  reverse_time=False, 
			  last_saved_time=None,
			  task_destination=None, 
			  zero_start=True):

		# constructor body
		self.task_name = task_name
		self.time_limited = time_limited
		self.amount_of_time = amount_of_time
		self.reverse_time = reverse_time
		self.last_saved_time = last_saved_time
		self.task_destination = task_destination
		self.zero_start = zero_start

	# setters
	def set_task_name(self, task_name):
		self.task_name = task_name

	def set_time_limited(self, value):
		self.time_limited = value

	def set_amount_of_time(self, amount_of_time):
		self.amount_of_time = amount_of_time

	def set_reverse_time(self, value):
		self.reverse_time = value

	def set_last_saved_time(self, time):
		self.last_saved_time = time

	def set_task_destination(self, time):
		self.task_destination = time

	def set_zero_start(self, value):
		self.zero_start = value

	# getters
	def get_task_name(self):
		return self.task_name

	def get_time_limited(self):
		return self.time_limited

	def get_amount_of_time(self):
		return self.amount_of_time

	def get_reverse_time(self):
		return self.reverse_time

	def get_last_saved_time(self):
		return self.last_saved_time

	def get_task_destination(self):
		return self.task_destination

	def get_zero_start(self):
		return self.zero_start

	# display task information
	def __str__(self):
		from utilities.validation import seconds_to_time_format
		if self.time_limited:
			time_direction = 'begining-end' if not self.reverse_time else 'end-beging'
			time_left = seconds_to_time_format(self.task_destination - self.last_saved_time)
			last_updated_time = seconds_to_time_format(self.last_saved_time)

			return "\n".join([f"- Task name: {self.task_name}", 
			 			f"- Time limited: {self.time_limited}", 
						f"- Time direction: {time_direction}",
						f"- Time amount: {self.amount_of_time}", 
						f"- Spended time: {last_updated_time}",
						f"- Time left: {time_left}"]
			)

		else:
			return f"- Task name: {self.task_name}\n- Time limited: {self.time_limited}"