from ui.ui_handler import clear_screen_and_print_title

from utilities.create_task import create_task
from utilities.load_data import load_create_task_text_data

from utilities.validation import number_validation


def back_to_main_menu():
    from ui.menu_navigation import main_menu_ui
    return main_menu_ui()

class CreateTaskUI:
    def __init__(self, 
            header,
            task_name=None,
            task_time_limited=None,
            task_amount_of_time=None,
            task_start_position=None,
            type_of_stopwatch=None):
        
        # set header
        self.header = header

        # set local variables
        self.task_amount_of_time = task_amount_of_time
        self.task_start_position = task_start_position
        self.task_time_limited = task_time_limited
        self.task_name = task_name
        self.type_of_stopwatch = type_of_stopwatch

        # load ui text component
        self.ui_text = load_create_task_text_data()
    
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
            back_to_main_menu()
        else:
            return self.create_task_ui()
    
    # type of stopwatch
    def select_type_of_stopwatch(self):

        '''
            check if select stopwatch '1 - regular' or '2 - time limited' 
            otherwise ask enter again
        '''

        ui_component = self.ui_text["select_type_of_stopwatch"]

        print(ui_component["type_of_stopwatch"])
        print("".join(ui_component["stopwatch_options"]["options"]))
        type_of_stopwatch = False if input(ui_component["stopwatch_options"]["selection"]) == '2' else True

        # if type_of_stopwatch not in ui_component["stopwatch_options"]["list"]:
        #     raise IndexError
        
        return type_of_stopwatch

    # time limited settings
    def time_limited_stopwatch(self):
        '''
            set time limited and start position properties
        '''
        ui_component = self.ui_text["time_limited_stopwatch"]
        def set_amount_of_time():
            '''
                set amout of time
                check if value is digit 
                othewise ask enter again
            '''

            task_amount_of_time = input(ui_component["set_amount_of_time"])
            if number_validation(task_amount_of_time):
                self.task_amount_of_time = task_amount_of_time    
            else:
                raise ValueError

        def set_start_positon():
            '''
                set start position 
                check if value is 'yes' or 'no'
                otherwise ask enter again
            '''
            task_start_positon = self.yes_and_no_validation(input(ui_component["set_start_position"]))
            self.task_start_positon = task_start_positon
            if self.task_start_positon:
                self.task_start_positon = True if self.task_start_positon == 'yes' else False
            else:
                self.continue_or_back_to_main_menu()

        if self.task_amount_of_time is None:
            set_amount_of_time()
        if self.task_start_position is None:
            set_start_positon()

        return not self.type_of_stopwatch

    def task_confirmation(self):
        ui_component = self.ui_text["task_confirmation"]
        option = input(ui_component["create_new_task"])
        confirm_task_creation = self.yes_and_no_validation(option)
        if not confirm_task_creation:
            self.continue_or_back_to_main_menu()
        
        return True if confirm_task_creation == "yes" else False

    def task_saving(self):
        ui_component = self.ui_text["task_saving"]
        create_task(
            task_name=self.task_name,
            time_limited=self.task_time_limited,
            amount_of_time=self.task_amount_of_time,
            start_position=self.task_start_position
        )

        print(ui_component["success"])
        input("press any button...")
        from ui.menu_navigation import task_menu_ui
        task_menu_ui(self.task_name)
        

    def input_task_name(self):
        ui_component = self.ui_text["input_task_name"]
        task_name = input(ui_component["enter_name"])

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

        # task info ui compomponent
        ui_component = self.ui_text["create_task_ui"]["task_info"]

        try:
            if self.task_name is None:
                self.header()
                # enter name of task
                self.task_name = self.input_task_name()

            if self.type_of_stopwatch is None:
                self.header()
                # select type of stopwatch
                self.type_of_stopwatch = self.select_type_of_stopwatch()
            
            if self.task_time_limited is None:
                self.header()
                # time limited stopwatch settings
                if self.type_of_stopwatch == False:
                    self.task_time_limited = self.time_limited_stopwatch()
                else:
                    self.time_limited_stopwatch = self.type_of_stopwatch
            
            # check task information
            self.header()
            print(ui_component["title"])
            print(ui_component["task_name"], self.task_name)
            print(ui_component["task_limited"], self.task_time_limited)
            if self.task_time_limited:
                print(ui_component["amount_of_time"], self.task_amount_of_time)
                print('{} {}'.format(ui_component["task_start_position"],
                    self.task_amount_of_time+':00' if self.task_start_position else '00:00'))

            if self.task_confirmation():
                self.task_saving()
            else:
                print("\n\nTask creating has been canceled.")
                input("press any button to back to main menu...")
                back_to_main_menu()
                
        except ValueError as ex:
            print("\nYou have to put a numeric value!")
            self.continue_or_back_to_main_menu()
        except IndexError:
            print("you selected value that not valid!\nplease select good one!")
            self.continue_or_back_to_main_menu()
