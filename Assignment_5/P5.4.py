"""
Sherman Yan
Assignment 5 - P5.4
Input:  String
Output: Middle character(s)
"""


##
# Main function
# ask for user to input a word and output the middle characters of that input
#
def main():
    userInput = input("Please enter a word: ")

    print("The middle character(s) of \"" + userInput + " is: " + middle(userInput))


##
# This function calculates for the middle two characters of the inputted word
# @param word
# @return middle character(s) as string
#
def middle(word):
    length = len(word)

    middle_index = length // 2

    if length % 2 == 0:
        return str(word[middle_index - 1] + word[middle_index])
    else:
        return str(word[middle_index])


if __name__ == '__main__':
    main()

"""
Sample Run
Please enter a word: middle
The middle character(s) of "middle is: dd
"""
