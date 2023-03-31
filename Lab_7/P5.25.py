"""
Sherman Yan, Junyan Wen
Lab 7 - P5.25
Input:  ZipCode
Output: Barcode
"""


##
# Main Function
# Inputs a barcode and prints the barcode
#

def main():

    ZIPCODE_LENGTH = 5
    inputZip = input("Enter a zip code (5 digit): ")

    while not checkInput(ZIPCODE_LENGTH, inputZip):
        print("Invalid.")
        inputZip = input("Enter a zip code (5 digit): ")

    print("BarCode : ",  printBarCode(inputZip)
)


##
# generates the digit of the barcode
# @param digit
# @return string of barcode for that digit
#
def printDigit(digit):
    if digit == "9":
        return "|:|::"
    elif digit == "8":
        return "|::|:"
    elif digit == "7":
        return "|:::|"
    elif digit == "6":
        return ":||::"
    elif digit == "5":
        return ":|:|:"
    elif digit == "4":
        return ":|::|"
    elif digit == "3":
        return "::||:"
    elif digit == "2":
        return "::|:|"
    elif digit == "1":
        return ":::||"
    elif digit == "0":
        return "||:::"


##
# Prints a barcode for the zipCode
# @param zipcode as string
# @return barcode as string

def printBarCode(zipCode):
    code = str(zipCode)
    n = 0

    for i in range(len(code)):
        n = n + int(code[i])

    if not n % 10 == 0:
        n = n % 10
        n = 10 - n
        code = code + str(n)

    res = "|"

    for i in range(len(code)):
        res += printDigit(code[i])

    res += "|"

    return res

##
# check input to make sure its length is = length
# @param length desired and the int to test
# @return true if condition met, else false
#
def checkInput(length, test):

    if len(str(test)) == int(length):
        return True
    else:
        return False


if __name__ == '__main__':
    main()


"""
Sample Code
Enter a zip code (5 digit): 134134214
Invalid.
Enter a zip code (5 digit): 95104
BarCode :  ||:|:::|:|::::||||::::|::|:::|||
"""