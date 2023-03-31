"""
Sherman Yan
Assignment 1 - P2.10
I:  cost, miles per year, gas price, mpg, resale
P:  Calculate cost of owning the car and total cost after 5 years
O:  Total cost owning the car for 5 years
"""

print("Cost of owning a car Calculator.")
print("Please enter the following:\nWhat is the...")

# input
cost = float(input("Cost of new car: "))
milesPerYear = float(input("Estimated miles driven per year: "))
gasPrice = float(input("Estimated gas price: "))
mpg = float(input("Efficiency in miles per gallon: "))
resale = float(input("Estimated resale value after five years: "))

# processing
owningCost = milesPerYear / mpg * gasPrice
totalCost = cost + owningCost - resale

# output
print("Your cost of owning a car after 5 years is: $%-.2f" % totalCost)

"""
Sample Run

Cost of owning a car Calculator.
Please enter the following:
What is the...
Cost of new car: 35000
Estimated miles driven per year: 5000
Estimated gas price: 5.30
Efficiency in miles per gallon: 45
Estimated resale value after five years: 18000
Your cost of owning a car after 5 years is: $17588.89

"""