import calendar


def weekday_of_birth_date(date):
    """Takes a date object and returns the corresponding weekday string"""
    y, m, d = date.year, date.month, date.day
    WEEKDAYS = ['Monday', 
                'Tuesday', 
                'Wednesday',
                'Thursday',
                'Friday',
                'Saturday',
                'Sunday']
    return WEEKDAYS[calendar.weekday(y, m, d)]