from datetime import datetime as dt


def lengthen_date(date_string):
    """Converts a date string from 'dd.mm.yyyy' format to a more verbose format.

    Args:
        date_string (str): A string representing a date in 'dd.mm.yyyy' format.

    Returns:
        str: A string representing the input date in a more verbose format. 
        The returned string is constructed by extracting the day name, 
        day of the month, month name, and year from the input date and concatenating
        them with appropriate separators and an ordinal suffix for the day of the month.
        Exception: If the input string is not in the correct format, 
        an exception is raised and returned.

    Examples:
        >>> lengthen_date('01.03.1968')
        'Friday 1st March 1968'
    """
    try:
        date = dt.strptime(date_string, '%d.%m.%Y')
        day_name = date.strftime('%A')
        day_of_month = int(date.strftime('%d'))
        month_name = date.strftime('%B')
        year = date.strftime('%Y')

        suffix = ''

        if day_of_month in (1, 21, 31):
            suffix = 'st'
        elif day_of_month in (2, 22):
            suffix = 'nd'
        elif day_of_month in (3, 23):
            suffix = 'rd'
        else:
            suffix = 'th'

        new_date = f'{day_name} {day_of_month}{suffix} {month_name} {year}'
        return new_date
    except Exception as e:
        return Exception



