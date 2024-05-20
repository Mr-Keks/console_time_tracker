def number_validation(number):
    '''
    check if number is digit value
    '''
    return number.isdigit

def add_zero(time):
        '''
            adding zero prefix
        '''
        time = str(time)
        if len(time) == 1:
            time = "0"+time
        return time

def str_time_format(str_time):
    '''
        time display: hours:minutes:seconds
        examples: 100:00:00; 00:45:00
    '''

    hours, minutes = str_time.split(":")

    return ":".join([add_zero(hours), add_zero(minutes), "00"])

def int_time_format(str_time):
    hours, minutes = str_time.split(":")
   
    return int(hours)*60*60 + int(minutes)*60

def seconds_to_time_format(seconds):
    hours = int(seconds // 3600)
    remaining_seconds = int(seconds % 3600)
    minutes = int(remaining_seconds // 60)
    seconds = int(remaining_seconds % 60)
    
    hours = add_zero(hours)
    minutes = add_zero(minutes)
    seconds = add_zero(seconds)

    return f"{hours}:{minutes}:{seconds}"
