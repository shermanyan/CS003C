"""
Sherman Yan, Junyan Wen
Lab 4 - P3.39
"""


def input_validation(valid_entry, max_attempts):

    # function to validate an input for valid_entry
    # if invalid entry, print (Your PIN is correct)
    # after max_attempts is reached, print (Your bank card is blocked)

    attempts = 0

    while not attempts > int(max_attempts):

        pin = input("Enter your PIN:")

        if pin == str(valid_entry):
            print("Your PIN is correct")
            break
        elif attempts < int(max_attempts):
            print("Your PIN is incorrect")
        else:
            print("Your bank card is blocked")

        attempts += 1


print("---ATM---")

# set variables
VALID_PIN = "1234"
NUM_ATTEMPTS = 3

# call function
input_validation(VALID_PIN, NUM_ATTEMPTS)


"""
Sample Run
---ATM---
Enter your PIN:123123
Your PIN is incorrect
Enter your PIN:123
Your PIN is incorrect
Enter your PIN:12
Your PIN is incorrect
Enter your PIN:3
Your bank card is blocked

"""
