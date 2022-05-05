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
SHEET = GSPREAD_CLIENT.open('my-company-data')

employees = SHEET.worksheet('Employees')

data = employees.get_all_values()


def welcome_text():
    """
    A welcome message will be printed and explaining which commands
    are available to extract certain data about employees.
    """
    print("Welcome to My Company Data\n")
    print("This program will give you a chance to extract\n")
    print("anonymous data about the employees of this company")
    print("The available commands are (type the number into the console):\n")
    print("1. Nationalities\n2. Genders\n3. Salary")
    get_input_data()


def get_input_data():
    """
    This input field will run the correct function
    dependant on if the value entered is valid.
    """
    command = input("Enter a number listed above to view the data\n")
    print("You have selected: " + command)

    while True:
        if command == 1:
            nationalities_data(1)
        elif command == 2:
            gender_data(2)
        elif command == 3:
            salary_data(3)
        
        if validate_input(True):
            print("Your input has been validated, printing data to terminal")
        break
    return command


def validate_input(values):
    try:
        if values != int(1 or 2 or 3):
            raise ValueError(
                'You have not entered one of the numbers provided above'
                )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again")
        return False

    return True


def nationalities_data():
    countries = employees.col_values(5)
    print("Nationalities selected")
    return countries


def gender_data():
    gender = employees.col_values(4)
    print("Genders selected")
    return gender
    print(gender)


def salary_data():
    salary = employees.col_values(6)
    print("Salaries selected")
    return salary
    print(salary)


welcome_text()
