"""
Sherman Yan
Lab 5 - P4.4
"""

MAX_NUM_OF_MONTHS = 12


def highest_month_value(number_of_months):

    current_month = 1
    highest_value = 0
    highest_month = 0

    while current_month <= number_of_months:

        current_value = float(input("Enter the value for month " + str("%.0f" % current_month) + ": "))

        if current_value >= highest_value:
            highest_value = current_value
            highest_month = current_month

        current_month += 1

    return highest_month


highestMonth = highest_month_value(MAX_NUM_OF_MONTHS)

print("The highest value is in month:", highestMonth)


"""
Sample Run
Enter the value for month 1: 1
Enter the value for month 2: 23
Enter the value for month 3: 5
Enter the value for month 4: 12
Enter the value for month 5: 3
Enter the value for month 6: 12
Enter the value for month 7: 6
Enter the value for month 8: 16
Enter the value for month 9: 12
Enter the value for month 10: 35
Enter the value for month 11: 1
Enter the value for month 12: 432
The highest value is in month: 12
"""