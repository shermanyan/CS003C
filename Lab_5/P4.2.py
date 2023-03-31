"""
Sherman Yan
Lab 5 - P4.2
"""


def integer_input(int_list):

    user_input = str(input("Please enter up to 10 integers with spaces in between each number:")) + " "

    current_num = ""

    for n in range(len(user_input)):
        if user_input[n].isnumeric():
            current_num += user_input[n]
        elif user_input[n].isspace() and user_input[n-1].isnumeric():
            int_list.append(int(current_num))
            current_num = ""
        else:
            print("Invalid Input.")
            int_list.clear()
            return integer_input(int_list)

    if len(int_list) > 10:
        print("Invalid, MAX input reached")
        int_list.clear()
        return integer_input(int_list)

    return int_list


def small_and_large(compare_list):

    print("%-20s" % "Smallest:", min(compare_list))
    print("%-20s" % "Largest:", max(compare_list))


def num_even_odd(compare_list):

    even = 0
    odd = 0

    for i in range(len(compare_list)):
        if compare_list[i] % 2 == 0:
            even += 1
        else:
            odd += 1

    print("%-20s" % "Number of Evens:", even)
    print("%-20s" % "Number of Odds:", odd)


def cumulative_totals(compare_list):

    print("%-20s" % "Cumulative totals:", end=" ")

    current = 0
    total = 0

    while current < len(compare_list):

        total += compare_list[current]
        print(total, end=" ")

        current += 1

    print("")


def adjacent_duplicates(compare_list):

    print_list = []
    print("%-20s" % "Adjacent duplicates:", end=" ")

    for i in range(1, len(compare_list)):
        if compare_list[i] == compare_list[i-1] and compare_list[i] not in print_list:
            print_list.append(compare_list[i])

    if print_list:
        print(*print_list + [" "])
    else:
        print("N/A")


# list for the input
inputIntegers = []

# input into list
integer_input(inputIntegers)

# print results
print("\n")
print("%-20s" % "Inputted:", *inputIntegers + [" "])
small_and_large(inputIntegers)
num_even_odd(inputIntegers)
cumulative_totals(inputIntegers)
adjacent_duplicates(inputIntegers)


"""
Sample Run
Please enter up to 10 integers with spaces in between each number:1 2 3 4 5 6 7 8 1 2 3
Invalid, MAX input reached
Please enter up to 10 integers with spaces in between each number:1 2 323 1 1 1 0


Inputted:            1 2 323 1 1 1 0  
Smallest:            0
Largest:             323
Number of Evens:     2
Number of Odds:      5
Cumulative totals:   1 3 326 327 328 329 329 
Adjacent duplicates: 1  
"""