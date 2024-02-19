from datetime import datetime

def check_date_format(date_string):
    '''
    This function checks if the parameter date_string is passed as 'YYYY-MM-DD', if the data
    passed are numbers and if the year, month and day are compatible and a valid date.
    If all the checks are passed this function returns True. Otherwise returns False.

    :param date_string: the date passed as a string in the format 'YYYY-MM-DD'.

    :return: True if all checks are passed. False otherwise.
    '''

    # Check if the date is passed as a string
    if not isinstance(date_string, str):
        return False

    # Check if the length of the string is exactly 10 characters
    if len(date_string) != 10:
        return False
    
    year, month, day = convert_date_string_to_parts(date_string)

    # Check if the year, month, and day fall within valid ranges
    if year < 1 or month < 1 or month > 12 or day < 1:
        return False
    
    # Check if the day is valid for the given month and year
    if day > 31 or (month in [4, 6, 9, 11] and day > 30) or \
       (month == 2 and (year % 4 != 0 or (year % 100 == 0 and year % 400 != 0)) and day > 28) or \
       (month == 2 and (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)) and day > 29):
        return False
    
    return True

def check_date_not_past(date_string):
    '''
    This function checks if the parameter date_string is the today date or in the future.
    If the check is passed this function returns True. Otherwise returns False.

    :param date_string: the date passed as a string in the format 'YYYY-MM-DD'.

    :return: True if the check is passed. False otherwise.
    '''

    year, month, day = convert_date_string_to_parts(date_string)

     # Get the current date
    current_date = datetime.now().date()

    # Convert the input date string to a datetime object
    input_date = datetime(year, month, day).date()

    # Check if the input date is today or in the future
    if input_date < current_date:
        return False
    
    return True
    
def convert_date_string_to_parts(date_string):
    '''
    This function converts the date passed as a string into 3 integers
    corresponding to year, month and day. It does not perform checks on the 
    correctness of the format of date passed as a parameter.

    :param date_string: the date passed as a string in the format 'YYYY-MM-DD'

    :return: 3 integers in the order year, month, day
    '''
    # Split the string into parts using '-' as the separator
    parts = date_string.split('-')
    
    # Check if there are exactly three parts
    if len(parts) != 3:
        return None
    
    # Check if each part is a valid integer
    for part in parts:
        if not part.isdigit():
            return None
    
    # Convert the parts to integers
    return map(int, parts)
    
    
