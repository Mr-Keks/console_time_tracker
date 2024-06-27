import time

from ui.ui_handler import clear_screen_and_print_title

class Stopwatch:
	'''
	Stopwatch class for tracking time.

	Logic explanation:
	1. take start values 
	For start program we need last updated time and destination time (if it's time limited)
	In method start
		1) if it's regular stopwatch then we calculate time next:
			- take current time (since epoch) and minus time what we already have (last updated)
		2) if it's time with destination then we calculate time next:
			- take current last updated time and minus destination time to check difference 
			  between them
			- and this differece we plus to current time (since epoch) to add this difference to 
			  current time

	In method elapsed
		1) if it's regular stopwatch
			- we minus current time (since epoch) from start time what we calculated before
		2) if it's time with destination
			- we minus current time (since epoch) from start time what we calculated before
			- and this difference minus destination time

	Examples:
		Regular stopwatch
			Let's:
				- time since epoch 	= 100
				- start time 		= 3
				
			In method start
				1) 100 - 3 = 97 -- start_time 

			Let's one second is already pass, then
			In method elapsed
				1)  101 - 97 = 4 -- last updated time

			Result:
				1) time we started 	= 3
				2) time we finished = 4

		Time limited stopwatch
			Let's:
				- time since epoch 	= 100
				- start time 		= 3
				- destination time 	= 10 

			In method start
				1) 100 + (3 - 10) = 93 -- start time

			Let's one second is already pass, then
			In method elapsed
				1) 10 - (101 - 93) = 2 -- last updated time

			Result
				1) time we stared 	= 3
				2) time we finished = 2
	'''
	def __init__(self, start_time, stop_time, reverse, zero_start):
		self.running = False
		if zero_start:
			self.start_time = 0
		else:
			self.start_time = start_time
		self.stop_time = stop_time
		self.reverse = reverse
		self.last_updated_time = None
		# time for comparing difference between start and stop
		self.st = None

	def elapsed_time(self):
		'''Get the elapsed time since the stopwatch started.'''
		if self.running:
			if self.reverse:
				return self.stop_time - (time.time() - self.start_time)
			else:
				return time.time() - self.start_time
		else:
			return 0

	def start(self):
		'''Start the stopwatch.'''
		if self.reverse:
			self.st = self.start_time
			self.start_time = time.time() + self.start_time # Adjust start time for reverse mode
			
		else:
			self.st = self.start_time
			self.start_time = time.time() - self.start_time
		self.running = True

	def stop(self):
		'''Stop the stopwatch.'''
		self.last_updated_time = self.elapsed_time()
		self.running = False

	def compare_times(self):
		return abs(self.st - self.last_updated_time)

	def display_compare_times(self):
		time_difference = self.compare_times()
		minutes = int(time_difference // 60)
		seconds = int(time_difference % 60)
		
		clear_screen_and_print_title()
		return f"You spended now: {minutes} minutes and {seconds} seconds!"

	def display_time(self):
		'''Display time including milliseconds.'''
		while self.running:
			elapsed_time = self.elapsed_time()
			minutes = int(elapsed_time // 60)
			seconds = int(elapsed_time % 60)
			milliseconds = int((elapsed_time - int(elapsed_time)) * 1000)
			print(f"\rTime: {minutes:02d}:{seconds:02d}:{milliseconds:03d}", end='', flush=True)
			time.sleep(0.001)  # Update milliseconds every 1 millisecond


def listen_for_enter(stopwatch):
	input()
	stopwatch.stop()
