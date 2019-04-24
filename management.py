import csv
from classes import *
from colorama import init, Fore
from datetime import datetime
from printers import print_error, print_roles, print_success_message
init()


def manage_user_action(user_choice, hospital):
    # Displays patient records
    if user_choice == "P1":
        with open("patientrecords.csv", "r") as file:
            records = list(csv.reader(file))
            for record in records:
                print(record)

    # Admits patient
    elif user_choice == "P2":
        # Obtains patient information
        patient_name = input(Fore.WHITE + "Patient's name: ")
        patient_age = input(Fore.WHITE + "Patient's age: ")
        cause_of_admission = input(Fore.WHITE + "Cause of admission: ")
        # Creates a new instance of a Patient
        patient = Patient(patient_name, patient_age, cause_of_admission)
        # Admits patient
        hospital.admit_patient(patient)
        print_success_message("admitted", patient_name)

    # Discharges patient
    elif user_choice == "P3":
        # Obtains patient information (name/id?)
        patient_id = input(Fore.WHITE + "Patient's id: ")
        # Search for patient
        search_result = search_patient(patient_id)
        if search_result:
            # Discharges patient
            # Updates patient record
            search_result[-2] = datetime.now()
            search_result[-1] = "discharge"
            print(search_result)
            hospital.discharge_patient(search_result)
            print_success_message("discharged", search_result[1])

        else:
            print_error("Patient not found")

    # Displays employee records
    elif user_choice == "E1":
        with open("employeerecords.csv", "r") as file:
            records = list(csv.reader(file))
            for record in records:
                print(record)

    # Hires employee
    elif user_choice == "E2":
        # Obtains employee information
        employee_name = input(Fore.WHITE + "Employee's name: ")
        employee_age = input(Fore.WHITE + "Employee's age: ")

        # Obtains the role of the new employee
        print_roles()
        employee_role = input(
            "Employee's role: ")

        if employee_role == "1":
            department = input(
                Fore.WHITE + "Which department is the doctor in? ")
            employee = Doctor(department, employee_name, employee_age)

        elif employee_role == "2":
            rank = input(Fore.WHITE + "What is the nurse's rank? ")
            employee = Nurse(rank, employee_name, employee_age)

        elif employee_role == "3":
            floor = input(
                Fore.WHITE + "Which floor does the janitor work on? ")
            employee = Janitor(floor, employee_name, employee_age)

        else:
            print_error("Invalid choice")

        employee_username = input(Fore.WHITE + "Choose a username: ")
        employee_pw = input(Fore.WHITE + "Enter a password: ")
        hospital.hire_employee(
            employee, "hire", employee_username, employee_pw)
        print_success_message("hired", employee_name)

    # Fires employee
    elif user_choice == "E3":
        # Searches the database for employee information
        employee_id = input(Fore.WHITE + "Employee's id: ")
        search_result = search_employee(employee_id)
        # If employee is found, update database
        if search_result:
            search_result[2] = "fire"
            hospital.fire_employee(search_result)
            print_success_message("fired", search_result[1])
        # Else, print error msg
        else:
            print_error("Employee not found")

    # Exits system
    elif user_choice == "4":
        return False
    # Prints error message
    else:
        print_error("Invalid choice")


def search_patient(patient_id):
    with open("patientrecords.csv", "r") as file:
        records = list(csv.reader(file))
        for record in records:
            # Searches for patient id
            if patient_id == record[0]:
                # Gets the role of the employee
                return record
        # Did not match any of the records
        return False


def search_employee(employee_id):
    with open("employeerecords.csv", "r") as file:
        records = list(csv.reader(file))
        for record in records:
            # Searches for employee id
            if employee_id == record[0]:
                # Gets the role of the employee
                return record
        # Did not match any of the records
        return False
