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


