"""
Here are the imports needed for the program to connect
with Google Sheets API and Gspread
"""
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)


def welcome_text():
    """
    A welcome message will be printed and explaining which commands
    are available to extract certain data about employees.
    """
    print("Welcome to My Company Data\n")
    print("This program will give you a chance to extract")
    print("anonymous data about the employees of this company\n")
    print("The available commands are (type the number into the console):\n")
    print("1. Nationalities\n2. Genders\n3. Salary")
    get_input_data()


def validate_input(values):
    """
    This function validates the user input
    from the get_input_data function asking if the user
    has entered either 1, 2, or 3, else print out an error message
    """
    if values not in ['1', '2', '3']:
        print("Invalid data, please try again")
        return False
    return True


def get_input_data():
    """
    Here the user input is stored in the variable command
    which will be passaed through the validate_input function
    and then run another function based on the choice the user made.
    """
    command = input("Enter a number listed above to view the data\n")

    print("You have selected: " + command)

    if validate_input(command):
        print("Your input has been validated, printing data to terminal")
        if command == '1':
            nationalities_data()
        elif command == '2':
            gender_data()
        elif command == '3':
            salary_data()
    else:
        get_input_data()


def fetch_new_data():
    """
    This function will fetch fresh data from the Google Sheets worksheet
    when the user makes an input to print out data
    """
    sheet = GSPREAD_CLIENT.open('my-company-data')
    return sheet.worksheet('Employees')


def nationalities_data():
    """
    Prints out statistical calculations of the employees
    based on their nationalities
    """
    print("Nationalities selected")
    employees = fetch_new_data()
    countries = employees.col_values(5)
    print(countries[1:])
    return countries


def gender_data():
    """
    Prints out statistical calculations of the employees
    based on their genders
    """
    print("Genders selected")
    employees = fetch_new_data()
    gender = employees.col_values(4)
    del gender[0]
    males = gender.count('Male')
    females = gender.count('Female')
    total = len(gender)
    percentage_male = males / len(gender)
    perc_male = format(percentage_male, '%')
    percentage_female = females / len(gender)
    perc_female = format(percentage_female, '%')
    print(f"There are a total of {total} employees at the company")
    print(f"{females} females and {males} males")
    print(f"The percentage of females are {perc_female}")
    print(f"The percentage of males are {perc_male}")
    return gender


def salary_data():
    """
    Prints out statistical calculations of the employees
    based on their salaries
    """
    print("Salaries selected")
    employees = fetch_new_data()
    salary = employees.col_values(6)
    del salary[0]
    salary_int = list(map(int, salary))
    salary_total = sum(salary_int)
    avg_salary = salary_total / len(salary_int)
    low_salary = min(salary_int)
    high_salary = max(salary_int)
    print(f"The average monthly salary at the company is: ${avg_salary}")
    print(f"The lowest monthly salary is: ${low_salary}")
    print(f"The highest monthly salary is: ${high_salary}")
    return salary_int


def main():
    """
    Run all functions
    """
    welcome_text()


if __name__ == '__main__':
    main()
