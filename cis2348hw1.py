from datetime import date

today = date.today()
# This shows the current date so the user knows what the date is
print("Welcome to the birthday calculator!")
# Asking user for name
name = input("What is your name: ")
print('Lets figure out how old you are', name)

print("Please enter the credentials in this format. M/D/YYYY")
print('Enter the current date')
print("Today's date is:", today)
# Prompt user for current date
# Going to keep everything one line so adding the int function so user can only enter an integer
currentdate_month = int(input('Month: '))
currentdate_day = int(input("Day: "))
currentdate_year = int(input("Year: "))
# Prompt user for birthday
print('Enter your birthday')
bday_month = int(input("Month: "))
bday_day = int(input("Day: "))
bday_year = int(input("Year: "))

# Have to subtract the birthday year from the current year to determine the difference

determine_age = currentdate_year - bday_year

if bday_day == currentdate_day and bday_month == currentdate_month:
    print("Happy birthday", name)
    # If dates match, then it is the users birthday
    # If dates do not match, then is not the users birthday
else:
    print('It is currently not your birthday')

print('From the information you have given us,  you', name, 'are currently', determine_age, 'years old.')