"""
Sherman Yan
Assignment 8 - Fraction class tester
"""

##
# Test each of the overload operators in the Fraction class
#

from fraction import Fraction

a = Fraction(1, 6)
b = Fraction(1, 3)
value1 = Fraction(7, 9)
value2 = Fraction(-5, 12)
value3 = Fraction(4, 8)

# adding
c = a + b
print(c)
print("Expected: 1/2\n")

# adding and subtracting
result = value1 + value2 - value3
print(result)
print("Expected: -5/36\n")

# comparing
if result < value1 or result < value2 :
   print("less than")
else :
   print("not less than")
print("Expected: less than\n")

# converting to float
print("%.2f" % float(result))
print("Expected: -0.14\n")

# multiplying
print(value1 * value1)
print("Expected: 49/81\n")

# dividing
print(value1 / value3)
print("Expected: 14/9\n")

# unary minus
print(-value1)
print("Expected: -7/9\n")

# comparison
print(value3 == value1)
print("Expected: True\n")
print(value1 == value2)
print("Expected: False\n")



"""
Sample Run
1/2
Expected: 1/2

-5/36
Expected: -5/36

less than
Expected: less than

-0.14
Expected: -0.14

49/81
Expected: 49/81

14/9
Expected: 14/9

-7/9
Expected: -7/9

True
Expected: True

True
Expected: False
"""