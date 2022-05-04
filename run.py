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

    if command == 1:
        nationalities_data()
    elif command == 2:
        gender_data()
    elif command == 3:
        salary_data()


def validate_input():
    try:
        if command != int(1, 2, 3):
            raise ValueError(
            f"You have not entered one of the numbers provided above, please try again"
        )
    except ValueError as e:
        print(f"You need to use ")


def nationalities_data(data):
    countries = employees.col_values(5)


def gender_data(data):
    gender = employees.col_values(4)


def salary_data(data):
    salary = employees.col_values(6)


welcome_text()