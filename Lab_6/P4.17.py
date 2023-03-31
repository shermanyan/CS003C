"""
Sherman Yan
Lab 6 - P4.17
"""


def get_primes(number):

    prime_list = []

    for i in range(2, number + 1):
        for n in range(2, i):
            if i % n == 0:
                break
        else:
            prime_list.append(i)

    return prime_list


userInput = int(input("Please enter an integer: "))

primes = get_primes(userInput)

print("The prime number(s) for", userInput, "are:", *primes)

"""
Sample Run
Please enter an Integer: 10
The prime number(s) for 10 are: 2 3 5 7
"""