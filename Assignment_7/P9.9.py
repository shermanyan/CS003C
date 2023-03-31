"""
Sherman Yan
Assignment 7 - P9.9
"""


##
# creates a lock with features
#
class ComboLock:
    ##
    # constructs list for order and code
    #
    def __init__(self):
        self._code = []
        self._order = []

    ##
    # sets the code for the lock
    # @param: secret1, secret2, secret3 stores the code for the lock
    #
    def ComboLock(self, secret1, secret2, secret3):
        self._code = [secret1, secret2, secret3]

    ##
    # clears order and code list
    #
    def reset(self):
        self._order.clear()

    ##
    # appends 'left', ticks to order list
    # @param: ticks number turned to on lock
    #
    def turnLeft(self, ticks):
        if not 0 < ticks < 39:
            raise ValueError(", out of range")
        self._order.append(['left', ticks])

    ##
    # appends 'right', ticks to order list
    # @param: ticks number turned to on lock
    #
    def turnRight(self, ticks):
        if not 0 < ticks < 39:
            raise ValueError(", out of range")
        self._order.append(['right', ticks])

    ## checks if the lock can be opened from code and order lists
    # @return true or false based on whether condition matched
    #
    def open(self):
        if len(self._order) == len(self._code) and \
                self._order[0][0] == 'right' and self._order[1][0] == 'left' and self._order[2][0] == 'right':
                for i in range(len(self._order)):
                    if self._order[i][1] == self._code[i]:
                        break
                else:
                    return False
                return True
        return False


def main():
    lock = ComboLock()
    lock.ComboLock(10, 20, 30)

    count = 1

    while count <= 3:
        try:
            print("Enter Combination #", count)
            turn = (input("L or R, or C to clear: "))
            if turn.upper() == 'C':
                lock.reset()
                count = 1
            else:
                if 'L' != turn.upper() != 'R':
                    raise NameError('Invalid turn option')
                else:
                    amount = float(input("Amount: "))
                if turn.upper() == 'R':
                    lock.turnRight(amount)
                else:
                    lock.turnLeft(amount)
                count += 1
        except NameError as error:
            print("ERROR: " + str(error))

        except ValueError as val:
            print("ERROR: Invalid Input" + str(val))

    if lock.open():
        print("Unlocked")
    else:
        choice = input('Invalid, try again? Y/N: ')
        if choice.upper() == 'Y':
            main()

main()

"""
Sample Run

Enter Combination # 1
L or R, or C to clear: l
Amount: 10
Enter Combination # 2
L or R, or C to clear: r
Amount: 20
Enter Combination # 3
L or R, or C to clear: r
Amount: 10
Invalid, try again? Y/N: y
Enter Combination # 1
L or R, or C to clear: 10
ERROR: Invalid turn option
Enter Combination # 1
L or R, or C to clear: r
Amount: 1-
ERROR: Invalid Inputcould not convert string to float: '1-'
Enter Combination # 1
L or R, or C to clear: r
Amount: 10
Enter Combination # 2
L or R, or C to clear: l
Amount: 20
Enter Combination # 3
L or R, or C to clear: r
Amount: 30
Unlocked
"""