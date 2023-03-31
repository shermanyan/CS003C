"""
Sherman Yan
Assignment 1 - P2.16
I:  5-digit number
P:  add spaces between each digit
O:  pi i
"""

# input
userInput = input("Enter 5 digit number:")

# Processing, can be done with a loop at higher levels
userInput = userInput[0] + " " + userInput[1] + " " + userInput[2] + " " + userInput[3] + " " + userInput[4]

# Output
print(userInput)

"""
Sample Run
Enter 5 digit number:11111
1 1 1 1 1
"""