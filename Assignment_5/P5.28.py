"""
Sherman Yan
Assignment 5 - P5.28
Input:  Income and number of children
Output: Aid amount
"""


##
# Main function
# ask for user to input income and number of children
# ends when -1 is entered
# displays aid amount
#
def main():

    famNum = 1
    print("- Aid Calculator - ")
    print("Mark end of input with -1")
    print("Please enter information for:")

    userinput = getIncomeAndChildren(famNum)

    while userinput:

        aid = calcAidAmt(userinput[0], userinput[1])

        print("Amount aid: $%.2f" % float(aid))

        famNum += 1
        userinput = getIncomeAndChildren(famNum)

    print("- Thanks Bye")


##
# asks for income and number of children
# @param input number, type int
# @return as list [income, number of children]
#
def getIncomeAndChildren(inputNumber):

    income = 0
    numChildren = 0
    print("- Family " + str(inputNumber))

    userInput = float(input("Enter Income: "))
    valid = validateInput(userInput, -1, float('inf'))

    while not valid:
        print("Invalid.")
        userInput = float(input("Enter Income: "))
        valid = validateInput(userInput, -1, float('inf'))

    if userInput == -1:
        return False
    else:
        income = userInput

    userInput = float(input("Enter Number of Children: "))
    valid = validateInput(userInput, -1, float('inf'))

    while not valid:
        print("Invalid.")
        userInput = float(input("Enter Number of Children: "))
        valid = validateInput(userInput, -1, float('inf'))

    if userInput == -1:
        return False
    else:
        numChildren = userInput

    return [income, numChildren]


##
# validates test is between smallest and largest
# @param test, the number to test, type int
# @param smallest, the min allowable test case, type int
# @param largest, the max allowable test case, type int
# @return true or false
#
def validateInput(test, smallest, largest):

    if smallest <= test <= largest:
        return True
    else:
        return False


##
# calculates aid amount
# @param income, type float
# @param children, type int
# @return aid amount
#
def calcAidAmt(income, children):

    if 30000 < income < 40000 and children >= 3:
        return children * 1000
    elif 20000 < income < 30000 and children >= 2:
        return children * 1500
    elif income < 20000:
        return children * 2000
    else:
        return 0


if __name__ == '__main__':
    main()

"""
Sample Run
- Aid Calculator - 
Mark end of input with -1
Please enter information for:
- Family 1
Enter Income: 10000
Enter Number of Children: 12
Amount aid: $24000.00
- Family 2
Enter Income: 0
Enter Number of Children: 4
Amount aid: $8000.00
- Family 3
Enter Income: -1
- Thanks Bye
"""