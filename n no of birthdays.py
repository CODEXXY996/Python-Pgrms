def get_birth():
    no = int(input("Enter the number of birthdays: "))
    birthdays = {}
    for i in range(no):
        name = input("Enter the name: ")
        dob = input("Enter the date of birth (dd/mm/yy): ")
        birthdays[name] = dob
    return birthdays

def print_birthdays(birthdays):
    for key in birthdays:
        date_parts = birthdays[key].split('/')
        day, month, year = date_parts
        print(f"The birthday of {key} is {day}-{month}-{year}")

birthdays = get_birth()
print_birthdays(birthdays)