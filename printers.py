from colorama import init, Fore
init()


def print_employee_menu():
    print(Fore.GREEN + "E1. View employee records\nE2. Hire employee\nE3. Fire employee\n")


def print_greeting(role):
    print(Fore.RED +
          f"==============================\nWELCOME BACK {role.upper()}\n==============================\n")


def print_header(hospital_name):
    print(Fore.BLUE +
          f"||==============================||\n||WELCOME TO {hospital_name.upper()}||\n||==============================||\n Please log in before proceeding.\n")


def print_patient_menu():
    print(Fore.GREEN + "P1. View patient records\nP2. Admit patient\nP3. Discharge patient\n")


def print_roles():
    print(Fore.YELLOW + "1. Doctor\n2. Nurse\n3. Janitor\n")


def print_success_message(action, person):
    print(f"You have successfully {action} {person}.")


def print_error(error_msg):
    print(
        f"---------------------------------------------------------\nSorry an error occurred.\n(Error: {error_msg})\nPlease try again.\n---------------------------------------------------------\n")
