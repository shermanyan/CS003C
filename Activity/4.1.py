
## Prints the smallest of the arguments
# @param x,y,z the arguments
# @return the smallest of the arguments

def smallest(x, y, z):

    return min(x, y, z)

## Prints the average of the arguments
# @param x,y,z the arguments
# @return the average of the arguments


def average(x, y, z):

    return (x + y + z) / 3


def main():

    print(smallest(1, 2, 3))

    print(average(1, 2, 3))


main()
