"""
Sherman Yan
Assignment 7 - P7.13
"""


##
# main function
# aks for input until there are no more inputs, then compute and print sum of the inputs
#
def main():

    total = 0
    print("Generate a sum of the floating-point numbers ")

    userInput = getInput()

    while userInput:
        total += userInput
        userInput = getInput()

    print("Total: %.2f" % total)


##
# gets input
# if input is not a float, ask for new input, max 2 error
# @param errors default is 0
# @return input or null
#
def getInput(errors=0):

    try:
        userinput = float(input("Please enter a floating-point number: "))
        return userinput
    except ValueError:
        if errors < 1:
            print("ERROR: Please enter a valid number")
            return getInput(1)  # call function with 1 error
    return


if __name__ == '__main__':
    main()


"""
Sample Code

Generate a sum of the floating-point numbers 
Please enter a floating-point number: 10
Please enter a floating-point number: 10
Please enter a floating-point number: 10
Please enter a floating-point number: 10
Please enter a floating-point number: 10
Please enter a floating-point number: 10
Please enter a floating-point number: s
ERROR: Please enter a valid number
Please enter a floating-point number: asf
Total: 60.00

"""