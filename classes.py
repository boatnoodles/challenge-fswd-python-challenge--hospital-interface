import csv
from datetime import datetime
from random import randint


class Hospital():
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def admit_patient(self, patient):
        with open("patientrecords.csv", "a") as file:
            writer = csv.writer(file)
            writer.writerow((patient.id, patient.name, patient.age,
                             patient.cause, datetime.now(), "admit"))

    def discharge_patient(self, search_result):
        with open("patientrecords.csv", "a") as file:
            writer = csv.writer(file)
            writer.writerow((search_result))

    def hire_employee(self, employee, action, username, password):
        with open("employeerecords.csv", "a") as file:
            writer = csv.writer(file)
            writer.writerow((employee.id, employee.name, employee.role,
                             action, username, password))

    def fire_employee(self, search_result):
        with open("employeerecords.csv", "a") as file:
            writer = csv.writer(file)
            writer.writerow(search_result)

    def login(self, username, password):
        with open("employeerecords.csv", "r") as file:
            records = list(csv.reader(file))
            for record in records:
                # Checks if username and password are correct
                if username in record[-2] and password in record[-1]:
                    # Gets the role of the employee
                    return record[2]
            # Did not match any of the records
            return False


class Patient():
    def __init__(self, name, age, cause):
        self.id = randint(1, 1000)
        self.name = name
        self.age = age
        self.cause = cause

    def __str__(self):
        return f"Patient {self.name}, {self.age} years old with cause of admission{self.cause}"


class Employee():
    def __init__(self, name, age, role):
        self.id = randint(1, 1000)
        self.name = name
        self.age = age
        self.role = role
        self.date_of_hire = datetime.now()

    def record_attendance(self, action):
        with open("employeeattendance.csv", "a") as file:
            writer = csv.writer(file)
            writer.writerow((self.name, datetime.now(), action))


class Doctor(Employee):
    def __init__(self, department, name, age):
        role = 'doctor'
        Employee.__init__(self, name, age, role)
        self.department = department


class Nurse(Employee):
    def __init__(self, rank, name, age):
        role = 'nurse'
        Employee.__init__(self, name, age)
        self.rank = rank


class Janitor(Employee):
    def __init__(self, floor, name, age):
        role = 'janitor'
        Employee.__init__(self, name, age, role)
        self.floor_in_charge = floor
