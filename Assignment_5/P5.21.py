"""
Sherman Yan
Assignment 5 - P5.21
Input:  A number
Output: Roman numeral conversion of inputted number
"""


##
# Main function
# ask for user to input a number to convert to roman numerals
# displays the roman numeral of the input
#
def main():
    userInput = int(input("Enter a number up to 3999 to convert to roman numerals: "))

    while not validateInput(userInput, 0, 3999):
        print("Invalid Input")
        userInput = int(input("Enter a number up to 3999 to convert to roman numerals: "))

    print(str(userInput) + " in Roman Numerals is: " + romanNumberToArabic(userInput))


##
# Converts a number 1-9 to roman based on string.
# @param n, a number to convert type int
# @param one, roman numerals. ie"I"
# @param five, roman numerals. ie"V"
# @param ten, roman numerals. ie"X"
# @return roman numeral of the inputted n
#
def romanDigit(n, one, five, ten):

    roman = ""
    if n > 8:
        return romanDigit(10-n, one, five, ten) + ten
    if n > 5:
        n -= 5
        roman += five
    if n <= 3:
        roman += one * n
    else:
        return romanDigit(5-n, one, five, ten) + five

    return roman


##
# converts a number (max 3999) to arabic
# @param number, type int max 3999
# @return roman numerals, type string
#
def romanNumberToArabic(number):

    roman = ""
    roman = romanDigit((number % 10), "I", " V", "X") + roman
    number = number // 10
    roman = romanDigit((number % 10), "X", " L", "C") + roman
    number = number // 10
    roman = romanDigit((number % 10), "C", "D", "M") + roman
    number = number // 10
    roman = romanDigit((number % 10), "M", "", "") + roman

    roman = roman.replace(" ", "")

    return roman


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


if __name__ == '__main__':
    main()

"""
Sample Run
Enter a number up to 3999 to convert to roman numerals: 39999
Invalid Input
Enter a number up to 3999 to convert to roman numerals: 2934
2934 in Roman Numerals is: MMCMXXXIV

"""
