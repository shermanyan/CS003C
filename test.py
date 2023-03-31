

## P5.4
# This program asks for a word and prints the middle letter(s)
#
def middle(string):
    stringLength = int(len(string))
    if stringLength % 2 == 0:  # if there are an even number of characters
        firstChar = string[round(stringLength / 2) - 1]
        secondChar = string[round(stringLength / 2)]
        return firstChar, secondChar
    else:  # if there are an odd number of characters
        middleChar = string[round(stringLength // 2)]
        return middleChar
userInput = input("Enter a word: ")
result = middle(userInput)
print("The middle letter(s) is/are: ", result)
