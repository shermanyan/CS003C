"""
Sherman Yan
Lab 6 - P4.9
"""

userInput = input("Enter a word: ")

print("\"" + userInput + "\"" + " in reverse is:", end=" ")

for i in range(len(userInput) - 1, -1, -1):
    print(userInput[i], end="")

"""
Sample Run
Enter a word: yauiyfoidsh
"yauiyfoidsh" in reverse is: hsdiofyiuay
"""