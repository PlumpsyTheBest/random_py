"""
Name: Lesson4.py
Author: Alex
Date: 01/10/24
Description:
    This program manages a person's record using a dataclass to store personal details.
    The record includes forename, surname, age, username, password, and email.
"""

# Import dataclass
from dataclasses import dataclass


# Represents a person's record with personal and contact details.
@dataclass
class Person:
    forename: str
    surname: str
    age: int
    username: str
    password: str
    email: str

# Populate the record
def populate_person():
    forename = input("Enter forename: ")
    surname = input("Enter surname: ")
    age = get_valid_age()
    username = input("Enter username: ")
    password = get_valid_password()
    email = input("Enter email: ")

    # Create a Person object
    return Person(forename, surname, age, username, password, email)


# Get valid age
def get_valid_age():
    age = int(input("Enter age: "))
    while age > 110 or age < 0:
        age = int(input("Enter age: "))
    return age


# Get valid password
def get_valid_password():
    password = input("Enter password: ")
    while len(password) > 16 or len(password) < 8:
        password = input("Enter password: ")
    return password


# Get valid email
def get_valid_email():
    email = input("Enter email: ")
    email_array = email.split("@")
    while email_array[1] != "outlook.co.uk" and email_array[1] != "gmail.com":
        email = input("Enter email: ")
        email_array = email.split("@")
    return email
