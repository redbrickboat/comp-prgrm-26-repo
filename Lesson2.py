#!usr/bin/env python3

import locale
locale.setlocale(locale.LC_ALL, 'en_US')

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
current_year = input("Enter the current year: ")
birth_year = input("Enter your birth year: ")
age = int(current_year) - int(birth_year)

print("\n Hello " + first_name + " " + last_name + "!" + 
      "\n You are " + str(age) + " years old this year.")

age += 1

print(f"\n In the next year {int(current_year) + 1}, you will be {age} years old.")

print("\n Completed by, Brick Newman")
