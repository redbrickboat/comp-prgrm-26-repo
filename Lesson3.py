#!/usr/bin/env python3

print("Welcome to the Interest Calculator")
print()

choice = "y"
while choice.lower() == "y":

    monthly_investment = int(input("Please enter the monthly investment: "))
    while monthly_investment <= 0 or monthly_investment >= 50000:
        monthly_investment = int(input("Error: Please enter a monthly investment over 0 and under 50,000: "))
    yearly_rate = int(input("Please enter the yearly investment rate: "))
    while yearly_rate <= 0 or yearly_rate >= 15:
        yearly_rate = int(input("Error: Please enter a yearly rate over 0 and under 15: "))
    years = int(input("Please enter the number of years: "))
    while years <= 0:
        years = int(input("Error: Please enter a number of years greater than 0: "))

    monthly_rate = yearly_rate / 12 / 100
    months = years * 12

    future_value = 0.0  
    for month in range (1, months + 1):
        future_value += monthly_investment
        monthly_interest_amount = round(future_value * monthly_rate, 2)
        future_value+= monthly_interest_amount

        if month % 12 == 0:
            current_year = month // 12
            print(f"Year {current_year}: ${round(future_value, 2)}")

    print()

    print(f"Investment Duration in Years: {years}")
    print(f"Yearly Interest rate: {yearly_rate}%")
    print(f"Monthly Investment Amount: ${round (monthly_investment, 2)}")
    print(f"Total Amount of Investment After Compounding: ${round(future_value, 2)}")

    choice = input("Continue (y/n)?: ")

print("Completed by, Brick Newman")


