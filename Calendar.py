def is_leap_year(year):
    # Determines if a given year is a leap year
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

def get_first_day(year):
    # Formula to get the first day of the year (0 = Sunday, 1 = Monday...)
    y = year - 1
    day = (1 + y + (y // 4) - (y // 100) + (y // 400)) % 7
    return day

def print_calendar(start_year, end_year):
    # Main function to print the 400 year calendar
    months = ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"]
    
    for year in range(start_year, end_year + 1):
        print(f"\n{'='*15} YEAR {year} {'='*15}\n")
        first_day = get_first_day(year)
        days_in_month = [31, 29 if is_leap_year(year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        current_day = first_day

        for month in range(12):
            print(f"\n--- {months[month]} ---")
            print("Sun Mon Tue Wed Thu Fri Sat")
            print("    " * current_day, end="") # Print leading spaces
            
            for day in range(1, days_in_month[month] + 1):
                print(f"{day:3} ", end="")
                current_day += 1
                if current_day > 6:
                    current_day = 0
                    print()
            print()
            if __name__ == "__main__":
    # Generates a 400-year span (e.g., 2000 to 2400)
    print_calendar(2000, 2400)
