"""
Sherman Yan
Assignment 4 - P4.6
"""

first = True
minimum = 0

value = input("Enter value:")

while value:

    if first:
        minimum = value
        first = False
    elif value < minimum:
        minimum = value

    value = input("Enter value:")

print(minimum)


"""
Sample Run
Enter value:1
Enter value:2
Enter value:3
Enter value:4
Enter value:5
Enter value:6
Enter value:2
Enter value:3
Enter value:4
Enter value:2
Enter value:-2
Enter value:
-2
"""