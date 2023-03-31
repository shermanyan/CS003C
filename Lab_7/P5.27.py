"""
Sherman Yan, Junyan Wen
Lab7 - P5.27
"""


##
# main function
# inputs a roman numeral
# validates the input
# converts to arabic number
# prints the arabic number
#
def main():

    inputRoman = input('Enter a roman number: ')

    while not checkInputForAlphaOnly(inputRoman):
        print("Invalid Input")
        inputRoman = input('Enter a roman number: ')

    print('Corresponding decimal number: ', convertRomanToNum(inputRoman))


##
# checks test only has alphas
# @param test, as string
# @return true if there's something other than alpha, else return false
#
def checkInputForAlphaOnly(test):
    for i in range(len(test)):
        if not str(test[i]).isalpha() or str.islower(test[i]):
            return False
    else:
        return True


##
# convert roman letter to an integer
# @param roman letter as string
# @return value as integer
#
def getRomanValue(letter):
    if letter == 'M':
        return 1000
    elif letter == 'D':
        return 500
    elif letter == 'C':
        return 100
    elif letter == 'L':
        return 50
    elif letter == 'X':
        return 10
    elif letter == 'V':
        return 5
    elif letter == 'I':
        return 1


##
# converts roman numeral to arabic numbers
# @param roman as type string
# @return total as an int
#
def convertRomanToNum(roman):

    total = 0
    while roman:
        if len(roman) == 1 or getRomanValue(roman[0]) >= getRomanValue(roman[1]):
            total += getRomanValue(roman[0])
            roman = roman[1:len(roman)]
        else:
            difference = getRomanValue(roman[1]) - getRomanValue(roman[0])
            total += difference
            roman = roman[2:len(roman)]

    return total


if __name__ == '__main__':
    main()


"""
Sample Code
Enter a roman number: 2788fsa
Invalid Input
Enter a roman number: MMMDCCXXIV
Corresponding decimal number:  3724

"""