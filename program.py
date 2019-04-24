import csv
import datetime
from classes import *
from colorama import init, Fore
from management import *
from printers import *
init()


def main():
    while True:
        main_hospital = Hospital("Hospitable Hospital", "Damansara")
        # while True:
        # Prints header and instruction
        print_header(main_hospital.name)

        # Obtains username and password from the user
        username = input(Fore.WHITE + "Username: ")
        password = input(Fore.WHITE + "Password: ")
        # Attempts to login (returns the role of user)
        login_result = main_hospital.login(username, password)
        second_menu = True
        while second_menu == True:
            if login_result == "doctor" or login_result == "nurse":
                print_greeting(login_result)
                # If doctor, allow to view patient records
                print_patient_menu()
                print("4. Return to main menu\n5. Exit program")
                doctor_choice = input(
                    Fore.WHITE + "What would you like to do today? ")
                if doctor_choice == "4":
                    second_menu = False
                elif doctor_choice == "5":
                    return False
                else:
                    manage_user_action(doctor_choice, main_hospital)
            elif login_result == "super admin":
                print_greeting(login_result)
                print_patient_menu()
                print_employee_menu()
                print("4. Return to main menu\n5. Exit program")
                admin_choice = input(
                    Fore.WHITE + "What would you like to do today? ")
                if admin_choice == "4":
                    second_menu = False
                elif admin_choice == "5":
                    return False
                else:
                    manage_user_action(admin_choice, main_hospital)
            elif login_result == "janitor":
                print_error("Access denied")
            else:
                print_error("User not found")
                second_menu = False


main()
