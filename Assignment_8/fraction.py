##
#  This module defines the Fraction class.
#

## Defines an immutable rational number with common arithmetic operations.
#
class Fraction:
    ## Constructs a rational number initialized to zero or a user specified value.
    #  @param numerator the numerator of the fraction (default is 0)
    #  @param denominator the denominator of the fraction (cannot be 0)
    #
    def __init__(self, numerator=0, denominator=1):
        # The denominator cannot be zero.
        if denominator == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")

        # If the rational number is zero, set the denominator to 1.
        if numerator == 0:
            self._numerator = 0
            self._denominator = 1

        # Otherwise, store the rational number in reduced form.
        else:
            # Determine the sign.
            if (numerator < 0 and denominator >= 0 or
                    numerator >= 0 and denominator < 0):
                sign = -1
            else:
                sign = 1

            # Reduce to smallest form.
            a = abs(numerator)
            b = abs(denominator)
            while a % b != 0:
                tempA = a
                tempB = b
                a = tempB
                b = tempA % tempB

            self._numerator = abs(numerator) // b * sign
            self._denominator = abs(denominator) // b

    ## Adds a fraction to this fraction.
    #  @param rhsValue the right-hand side fraction
    #  @return a new Fraction object resulting from the addition
    #
    def __add__(self, rhsValue):
        num = (self._numerator * rhsValue._denominator +
               self._denominator * rhsValue._numerator)
        den = self._denominator * rhsValue._denominator
        return Fraction(num, den)

# updated
    ## Subtracts a fraction from this fraction.
    #  @param rhsValue the right-hand side fraction
    #  @return a new Fraction object resulting from the subtraction
    #
    def __sub__(self, rhsValue):
        # num = (self._numerator * rhsValue._denominator -
        #        self._denominator * rhsValue._numerator)
        # den = self._denominator * rhsValue._denominator
        # return Fraction(num, den)

        return self + (-rhsValue)

# updated
    ## Determines if this fraction is equal to another fraction.
    #  @param rhsValue the right-hand side fraction
    #  @return True if the fractions are equal
    #
    def __eq__(self, rhsValue):
        # return (self._numerator == rhsValue._numerator and
        #         self._denominator == rhsValue._denominator)

        return rhsValue < self or rhsValue > self

    ## Determines if this fraction is less than another fraction.
    #  @param rhsValue the right-hand side fraction
    #  @return True if if this fraction is less than the other
    #
    def __lt__(self, rhsValue):
        return (self._numerator * rhsValue._denominator <
                self._denominator * rhsValue._numerator)

    ## Determines if this fraction is not equal to another fraction.
    #  @param rhsValue the right-hand side fraction
    #  @return True if the fractions are not equal
    #
    def __ne__(self, rhsValue):
        return not self == rhsValue

    ## Determines if this fraction is less than or equal to another fraction.
    #  @param rhsValue the right-hand side fraction
    #  @return True if if this fraction is less than or equal to the other
    #
    def __le__(self, rhsValue):
        return not rhsValue < self

    ## Determines if this fraction is greater than another fraction.
    #  @param rhsValue the right-hand side fraction
    #  @return True if if this fraction is greater than the other
    #
    def __gt__(self, rhsValue):
        return rhsValue < self

        ## Determines if this fraction is greater than or equal to another fraction.

    #  @param rhsValue the right-hand side fraction
    #  @return True if if this fraction is greater than or equal to the other
    #
    def __ge__(self, rhsValue):
        return not self < rhsValue

    ## Converts a fraction to a floating-point number.
    #  @return the floating-point value of this fraction
    #
    def __float__(self):
        return self._numerator / self._denominator

    ## Gets a string representation of the fraction.
    #  @return a string in the format #/#
    #
    def __repr__(self):
        return str(self._numerator) + "/" + str(self._denominator)

# newly added
    ## multiplies two fractions together
    # @return multplied fraction as object
    #
    def __mul__(self, other):
        numer = self._numerator * other._numerator
        denom = self._denominator * other._denominator

        return Fraction(numer, denom)

# created
    ## divides two fractions
    # @return fraction as object
    #
    def __truediv__(self, other):
        num = self._numerator * other._denominator
        den = self._denominator * other._numerator

        return Fraction(num, den)

# created
    # ## adds - to the numerator of the fraction
    # @return negative fraction as object
    def __neg__(self):
        return Fraction(-self._numerator, self._denominator)




