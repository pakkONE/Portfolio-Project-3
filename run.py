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
    if values not in ['1', '2', '3']:
        print("Invalid data, please try again")
        return False
    return True


def get_input_data():
    """
    This input field will run the correct function
    dependant on if the value entered is valid.
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
    sheet = GSPREAD_CLIENT.open('my-company-data')
    return sheet.worksheet('Employees')


def nationalities_data():
    print("Nationalities selected")
    employees = fetch_new_data()
    countries = employees.col_values(5)
    print(countries)
    return countries


def gender_data():
    print("Genders selected")
    employees = fetch_new_data()
    gender = employees.col_values(4)
    print(gender)
    return gender


def salary_data():
    print("Salaries selected")
    employees = fetch_new_data()
    salary = employees.col_values(6)
    print(salary)
    return salary


def main():
    """
    Run all functions
    """
    welcome_text()


if __name__ == '__main__':
    main()
