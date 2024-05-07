from ui.ui_handler import clear_screen_and_print_title

from utilities.create_task import create_task


class CreateTaskUI:
    def __init__(self):
        # default properties
        self.task_amount_of_time=None
        self.task_start_positon=None
        self.task_time_limited = None
        self.task_name = None
        self.type_of_stopwatch = None

    # input validation

    def yes_and_no_validation(self, option):
        '''
            check if option is 'yes' or 'no'
            otherwise ask enter again
        '''
        if option.lower() in ["yes", "no"]:
            return option
        else:
            print("Please put down 'yes' or 'no'!")
            self.continue_or_back_to_main_menu()

    # stop or continue
    def continue_or_back_to_main_menu(self):

        '''
            This function call when user selected wrong value
            in list of option and offer try again or 
            back to main menu to call proper function
        '''

        user_choise = input("press any button continue or 0 to back to main menu...")

        if user_choise == '0':
            from ui.menu_navigation import main_menu_ui
            return main_menu_ui()
        else:
            return self.create_task_ui()

        
    # type of stopwatch
    def select_type_of_stopwatch(self):

        '''
            check if select stopwatch '1 - regular' or '2 - time limited' 
            otherwise ask enter again
        '''

        print("What kind of stopwatch you want create?")
        type_of_stopwatch = input("\t1) regular\n\t2) time limited ")

        if type_of_stopwatch not in ["1", "2"]:
            raise IndexError
        
        return type_of_stopwatch

    # time limited settings
    def time_limited_stopwatch(self):
        '''
            set time limited and start position properties
        '''
        def set_amount_of_time():
            '''
                set amout of time
                check if value is digit 
                othewise ask enter again
            '''
            task_amount_of_time = int(input("Set your time (minutes): "))

            # if not task_amount_of_time.isdigit():
            #     print("You have to enter numeric value!")
            #     self.continue_or_back_to_main_menu(self.create_task_ui)
            # else:
            #     self.task_amount_of_time = task_amount_of_time
            self.task_amount_of_time = task_amount_of_time

        def set_start_positon():
            '''
                set start position 
                check if value is 'yes' or 'no'
                otherwise ask enter again
            '''
            task_start_positon = self.yes_and_no_validation(input("Do you prefer start your time from end? (yes/no): "))
            self.task_start_positon = task_start_positon
            if self.task_start_positon:
                self.task_start_positon = True if self.task_start_positon == 'yes' else False
            else:
                self.continue_or_back_to_main_menu()

        if self.task_amount_of_time is None:
            set_amount_of_time()
        if self.task_start_positon is None:
            set_start_positon()

        return True

    def task_confirmation(self):
        option = input("Create new task? (yes/no): ")
        confirm_task_creation = self.yes_and_no_validation(option)
        if not confirm_task_creation:
            self.continue_or_back_to_main_menu()

        return confirm_task_creation

    def task_saving(self):
        create_task(
            task_name=self.task_name,
            time_limited=self.task_time_limited,
            amount_of_time=self.task_amount_of_time,
            start_position=self.task_start_positon
        )

        print("\n\nYou successfuly created new file!")
        input("press any button...")
        from ui.menu_navigation import task_menu_ui
        task_menu_ui(self.task_name)
        

    def enter_task_name(self):
        task_name = input("Enter your task name: ")

        if task_name == "":
            print("You cannot create task with empty name!")
            self.continue_or_back_to_main_menu()
        return task_name

    # main function
    def create_task_ui(self):
        '''
            All properties are None as default 
            When user enter invalid value then 'create_task_ui'
            will be call again and those properties
            what were set pass 'is None' condition
        '''
        clear_screen_and_print_title()
        print("\tTask creation menu\n")
        try:
            if self.task_name is None:
                # enter name of task
                self.task_name = self.enter_task_name()

            if self.type_of_stopwatch is None:
                # select type of stopwatch
                self.type_of_stopwatch = self.select_type_of_stopwatch()
            
            if self.task_time_limited is None:
                # time limited stopwatch settings
                if self.type_of_stopwatch == "2":
                    self.task_time_limited = self.time_limited_stopwatch()
                else:
                    self.time_limited_stopwatch = False
            
            # check task information
            print("\n\nYour tasks info:\n")
            print('Task name: ', self.task_name)
            print('Task limited: ', self.task_time_limited)
            if self.task_time_limited:
                print('Amount of lime: ', self.task_amount_of_time)
                print('Task start postion: {}'.format(
                    self.task_amount_of_time+':00' if self.task_start_positon else '00:00'))

            if self.task_confirmation() == "yes":
                self.task_saving()
        except ValueError:
            print("You have to enter numeric value!")
            self.continue_or_back_to_main_menu()
        except IndexError:
            print("you selected value that not valid!\nplease select good one!")
            self.continue_or_back_to_main_menu()
