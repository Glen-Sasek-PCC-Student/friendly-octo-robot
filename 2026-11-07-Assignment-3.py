# main function

DAY_NAMES = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
day_of_year_name = []
day_of_year_notes = []

def initialize_data():
    for day in range(1, 366):
        day_name = DAY_NAMES[(day - 1) % 7]
        day_of_year_name.append(day_name)
        day_of_year_notes.append("")

def main():
    initialize_data()
    while True:
        print("\nMenu:")
        print("1. View notes for a specific day")
        print("2. Add a note for a specific day")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            day = int(input("Enter the day of the year (1-365): "))
            if 1 <= day <= 365:
                print(f"Day {day} ({day_of_year_name[day - 1]}): {day_of_year_notes[day - 1]}")
            else:
                print("Invalid day. Please enter a number between 1 and 365.")
        elif choice == '2':
            day = int(input("Enter the day of the year (1-365): "))
            if 1 <= day <= 365:
                note = input("Enter your note: ")
                day_of_year_notes[day - 1] = note
                print(f"Note added for Day {day} ({day_of_year_name[day - 1]}).")
            else:
                print("Invalid day. Please enter a number between 1 and 365.")
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

        

main()