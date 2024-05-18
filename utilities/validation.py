def number_validation(number):
    '''
    check if number is digit value
    '''
    return number.isdigit

def time_format(str_time):
    hours, minutes = str_time.split(":")
   
    return int(hours)*60 + int(minutes)