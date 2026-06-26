def is_leap_year(year):
    # Determines if a given year is a leap year
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

def get_first_day(year):
    # Formula to get the first day of the year (0 = Sunday, 1 = Monday...)
    y = year - 1
    day = (1 + y + (y // 4) - (y // 100) + (y // 400)) % 7
    return day
