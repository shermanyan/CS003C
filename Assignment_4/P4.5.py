"""
Sherman Yan
Assignment 4 - P4.5
"""
# set
userInput = float(input("Please enter a floating-point value. To end, enter negative number: "))

total = 0
smallest = userInput
largest = userInput
inputCounter = 0

# check
while userInput > 0:

    total += userInput

    # compute smallest and largest
    if userInput < smallest:
        smallest = userInput
    if userInput > largest:
        largest = userInput

    # change
    inputCounter += 1

    userInput = float(input("Enter floating-point value: "))

inputRange = largest - smallest
average = total/inputCounter

# display results
print("\n-RESULTS-")
print("%-15s %10.2f" % ("Average:", average))
print("%-15s %10.2f" % ("Smallest:", smallest))
print("%-15s %10.2f" % ("Largest:", largest))
print("%-15s %10.2f" % ("Range:", inputRange))


"""
Sample Code
Please enter a floating-point value. To end, enter negative number: 1234
Enter floating-point value: 1234
Enter floating-point value: 1
Enter floating-point value: 234
Enter floating-point value: 12
Enter floating-point value: 34
Enter floating-point value: 12
Enter floating-point value: 34
Enter floating-point value: 1
Enter floating-point value: 34
Enter floating-point value: 1234
Enter floating-point value: 134
Enter floating-point value: -1

-RESULTS-
Average:            349.83
Smallest:             1.00
Largest:           1234.00
Range:             1233.00
"""
