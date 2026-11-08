# main function




DAY_NAMES = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
MONTH_NAMES = ["January", "February", "March", "April", "May", "June",
               "July", "August", "September", "October", "November", "December"]

MENU_CHOICES = {
    '1': "View notes for a specific day",
    '2': "Add a note for a specific day",
    '3': "Change year",
    '4': "Display 7 days starting from a specific day",
    '5': "Exit"
}

year = 2024  # Default year

day_of_year_name = []
day_of_year_notes = []

# credit to https://stackoverflow.com/questions/6054016/calculate-day-of-week-given-a-date-in-python
# credit copilot for the code below
# TODO: Test this function with various years to ensure it works correctly
def calc_first_day_of_year_name_index(year):
    # Calculate the index of the first day of the year (0=Monday, 6=Sunday)
    # Using Zeller's Congruence algorithm
    if year < 1583:
        raise ValueError("Year must be 1583 or later.")
    
    q = 1  # Day of the month
    m = 1  # January
    K = year % 100
    J = year // 100

    if m < 3:
        m += 12
        K -= 1

    f = q + ((13 * (m + 1)) // 5) + K + (K // 4) + (J // 4) - (2 * J)
    day_of_week_index = f % 7

    # Adjusting to make Monday=0, ..., Sunday=6
    return (day_of_week_index + 5) % 7


def initialize_data():
    for day in range(1, 366):
        day_name = DAY_NAMES[(day - 1) % 7]
        day_of_year_name.append(day_name)
        day_of_year_notes.append("")

def change_year(new_year):
    global year
    year = new_year
    first_day_index = calc_first_day_of_year_name_index(year)
    for day in range(1, 366):
        day_name = DAY_NAMES[(first_day_index + (day - 1)) % 7]
        day_of_year_name[day - 1] = day_name


def prompt_for_year():
    while True:
        try:
            new_year = int(input("Enter a new year (1583 or later): "))
            if new_year >= 1583:
                change_year(new_year)
                print(f"Year changed to {new_year}.")
                break
            else:
                print("Year must be 1583 or later. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid year.")


def get_month_index(year, day_of_year):
    # Determine if the year is a leap year
    is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    
    # Days in each month
    days_in_month = [31, 29 if is_leap_year else 28, 31, 30, 31, 30, 
                     31, 31, 30, 31, 30, 31]
    
    cumulative_days = 0
    for month_index, days in enumerate(days_in_month):
        cumulative_days += days
        if day_of_year <= cumulative_days:
            return month_index + 1  # Return month index (1-12)
    
    return None  # Invalid day_of_year


def get_day_of_month(year, day_of_year):
    # Determine if the year is a leap year
    is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    
    # Days in each month
    days_in_month = [31, 29 if is_leap_year else 28, 31, 30, 31, 30, 
                     31, 31, 30, 31, 30, 31]
    
    cumulative_days = 0
    for month_index, days in enumerate(days_in_month):
        cumulative_days += days
        if day_of_year <= cumulative_days:
            return day_of_year - (cumulative_days - days)  # Return day of the month
    
    return None  # Invalid day_of_year


def display_day(year, day_of_year):
    if 1 <= day_of_year <= 365:
        month_index = get_month_index(year, day_of_year)
        day_of_month = get_day_of_month(year, day_of_year)
        day_name = day_of_year_name[day_of_year - 1]
        note = day_of_year_notes[day_of_year - 1]
        print(f"Day {day_of_year} ({day_name}, {MONTH_NAMES[month_index - 1]} {day_of_month}): {note}")
    else:
        print("Invalid day. Please enter a number between 1 and 365.")

def display_7_days(year, day_of_year=1):
    print(f"\nDisplaying 7 days starting from Day {day_of_year} of Year {year}:")
    for i in range(7):
        current_day = day_of_year + i
        if current_day > 365:
            break
        display_day(year, current_day)

def display_menu():
    print("\nYEAR: ", year)
    for key, value in MENU_CHOICES.items():
        print(f"{key}. {value}")

def prompt_for_day():
    while True:
        try:
            day = int(input("Enter the day of the year (1-365): "))
            if 1 <= day <= 365:
                return day
            else:
                print("Invalid day. Please enter a number between 1 and 365.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def do_choice_display_day():
    day = prompt_for_day()
    display_day(year, day)

def do_choice_enter_note():
    day = prompt_for_day()
    note = input("Enter your note: ")
    day_of_year_notes[day - 1] = note
    print(f"Note added for Day {day} ({day_of_year_name[day - 1]}).")

def do_choice_change_year():
    prompt_for_year()

def do_choice_display_7_days():
    day = prompt_for_day()
    display_7_days(year, day)

def route_choice(choice):
    if choice == '1':
        do_choice_display_day()
    elif choice == '2':
        do_choice_enter_note()
    elif choice == '3':
        do_choice_change_year()
    elif choice == '4':
        do_choice_display_7_days()
    elif "Exit" == MENU_CHOICES.get(choice):
        print("Exiting the program.")
    else:
        print("Invalid choice. Please try again.")

def main():
    initialize_data()
    next = True
    while next:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        if "Exit" == MENU_CHOICES.get(choice):
            next = False
        route_choice(choice)    
main()