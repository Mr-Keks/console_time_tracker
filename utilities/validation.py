def number_validation(number):
    '''
    check if number is digit value
    '''
    return number.isdigit

def str_time_format(str_time):
    '''
        time display: hours:minutes:seconds
        examples: 100:00:00; 00:45:00
    '''

    hours, minutes = str_time.split(":")

    def add_zero(time):
        '''
            adding zero prefix
        '''
        if len(time) == 1:
            time = "0"+time
        return time
    
    return ":".join([add_zero(hours), add_zero(minutes), "00"])

def int_time_format(str_time):
    hours, minutes = str_time.split(":")
   
    return int(hours)*60 + int(minutes)