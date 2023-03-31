"""
Sherman Yan
Assignment 1 - P2.7
I:  Radius
P:  Calculate the area, circumference, volume,
    and surface area based on radius
O:  Area and Circumference of circle and
    Volume and Surface Area of Sphere
"""

from math import pi

# input
radius = input("Please enter a Radius between 0 and 100: ")

# processing
area = (pi * int(radius) ** 2)
circum = (pi * 2 * int(radius))
volume = (4 / 3 * pi * int(radius) ** 3)
surfaceA = (4 * pi * int(radius) ** 2)

# output
print("\nCircle")
print("%-12s %11.2f" % ("Area", area))
print("%-12s %11.2f" % ("Circumference", circum))

print("\nSphere")
print("%-12s %11.2f" % ("Volume", volume))
print("%-12s %11.2f" % ("Surface Area", surfaceA))

"""
Sample Run

Please enter a Radius between 0 and 100: 99

Circle
Area              30790.75
Circumference       622.04

Sphere
Volume          4064378.95
Surface Area     123163.00

"""
