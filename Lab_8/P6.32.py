"""
Sherman, Josiah, Junyan
Lab 8 PT2 - P6.32
"""

# global amount for discount
DISCOUNT_FRACTION = 0.20


##
# main function
# calls get input for inputs from user
# calculates discount amount using discountAmt
#
def main():
    prices = []
    isPets = []

    userInput = getInput()
    while userInput: # if userInput is true or has something. ie not False
        prices.append(userInput[0])  # index the tuple of the output
        isPets.append(userInput[1])  # index the tuple of the output
        userInput = getInput()

    discountAmt = discount(prices, isPets, len(prices))  # generate discount amount
    print("Discount amount: $%.2f" % discountAmt)  # display the output


##
# get price and whether is pet or not from user
# @param none
# @return false if -1 is entered or price and pet as tuple
#
def getInput():

    price = (input("Enter the price. ie.(1.00), or enter -1 to quit: "))
    if price == '-1':
        return False
    while not validMoney(price): # while not valid
        print("Invalid Input")
        price = (input("Enter the price. ie.(1.00), or enter -1 to quit: "))
        if price == '-1':
            return False

    pet = input("Is it a pet(y/n)?")
    while not (pet.upper() == 'Y' or pet.upper() == 'N'): # while not valid
        print("Invalid Input")
        pet = input("Is it a pet(y/n)?")

    return [float(price), pet.upper()]  # return as indexable tuple


##
# check if amount is between 0 and 1000 and that all digits are numeric
# @param amount
# return True if condition met else false
#
def validMoney(amount):
    if 0 <= float(amount) <= 1000:
        for i in range(len(amount)):
            if amount[i].isnumeric() or amount[i] == '.':
                return True
            else:
                return False

    return False


##
# calculate discount
# @param prices and isPets, as list, and number of items
# @return discount amount
def discount(prices, isPet, nItems):
    total = 0
    if 'Y' in isPet and nItems >= 5:
        for i in range(nItems):
            if isPet[i] != 'Y':
                total += prices[i]

    return total * DISCOUNT_FRACTION


if __name__ == '__name__':
    main()

"""
Sample Run
Enter the price. ie.(1.00), or enter -1 to quit: 123.1
Is it a pet(y/n)?y
Enter the price. ie.(1.00), or enter -1 to quit: 312
Is it a pet(y/n)?n
Enter the price. ie.(1.00), or enter -1 to quit: 12.21
Is it a pet(y/n)?n
Enter the price. ie.(1.00), or enter -1 to quit: 12
Is it a pet(y/n)?n
Enter the price. ie.(1.00), or enter -1 to quit: 6
Is it a pet(y/n)?y
Enter the price. ie.(1.00), or enter -1 to quit: -1
Discount amount: $67.24
"""