"""
Sherman Yan, Junyan Wen
LAB 4 - P3.38
"""

from ezgraphics import *
from math import *

# used num2word for converting money to words for check
from num2words import num2words

# max work hours and overtime rate
WORK_HOURS_PER_WEEK = 40
OVERTIME_RATE = 1.5

employeeName = input("Enter employee's name: ")
employeePay = float(input("Enter employee's hourly wage as a decimal (ie. 2.20 for $2.20): "))
workHours = float(input("Enter employee's hours worked last week: "))

# validate that work hours are not over 100
while not workHours < 100:
    print("Invalid entry.")
    workHours = float(input("Enter employee's hours worked last week: "))

print("Processing information....")

# calculate total pay
totalPay = workHours * employeePay

# if there's overtime, add extra pay for the overtime hours
if workHours > WORK_HOURS_PER_WEEK:
    totalPay += ((workHours - WORK_HOURS_PER_WEEK) * employeePay * (OVERTIME_RATE - 1))

# generate paycheck

print("Printing Paycheck.....")

# set check sizing
chequeWidth = 800
chequeHeight = 300

# create graphics window for displaying check
win = GraphicsWindow(chequeWidth, chequeHeight)
paycheck = win.canvas()

# draw border
borderSpace = 5
paycheck.setLineStyle("dashed")
paycheck.setLineWidth(2)
paycheck.drawRect(borderSpace, borderSpace, chequeWidth - borderSpace * 2, (chequeHeight - borderSpace * 2))

# draw header
paycheck.setLineStyle("solid")
paycheck.setFill("red4")
paycheck.setOutline("white")
paycheck.drawRect(10, 10, chequeWidth - 20, 20)
paycheck.setFill("none")

# print company name
paycheck.setOutline("black")
paycheck.setTextFont("times", "bold", 20)
paycheck.drawText(20, 35, "Paycheck Generator \n")
paycheck.setTextFont("times", "italic", 16)
paycheck.drawText(20, 60, "6429 Colorado St. \n"
                          "Santa Monica, CA 90402 \n")

# print cheque number
paycheck.setTextJustify("right")
paycheck.setTextAnchor("nw")
paycheck.setTextFont("helvetica", "normal", 16)
paycheck.drawText(chequeWidth - 200, 40, "Cheque No.")
paycheck.setTextAnchor("ne")
paycheck.setTextFont("courier", "normal")
paycheck.drawText(chequeWidth - 20, 40, "241")

# print pay date
paycheck.setTextAnchor("nw")
paycheck.setTextFont("helvetica", "normal", 16)
paycheck.drawText(chequeWidth - 200, 60, "Pay Date.")
paycheck.setTextAnchor("ne")
paycheck.setTextFont("courier", "normal")
paycheck.drawText(chequeWidth - 20, 60, "05/15/22")

# print pay amount
paycheck.setTextAnchor("sw")
paycheck.setTextFont("arial", "bold", 22)
paycheck.drawText(20, 160, "PAYEE:")

# Payee Name
paycheck.setTextAnchor("sw")
paycheck.setTextFont("arial", "normal", 16)
paycheck.drawText(115, 158, employeeName.upper())

# Amount
paycheck.setTextAnchor("se")
paycheck.setTextFont("arial", "bold", 22)
paycheck.drawText(600, 160, "AMOUNT:")
paycheck.setOutline("snow3")
paycheck.setFill("snow2")
paycheck.drawRect(610, 130, 175, 35)

paycheck.setOutline("black")
paycheck.setFill("black")
paycheck.setTextFont("arial", "normal", 16)
paycheck.setTextAnchor("nw")
paycheck.drawText(620, 138, "$ " + str("%.2f" % float(totalPay)))

# using num2words package
maxTextLength = 60
emptySpaces = 0

numberLength = len(num2words(totalPay, to="currency").upper())
# calculate if there are extra space in the line add * to fill up
if numberLength < maxTextLength:
    emptySpaces = floor((maxTextLength - numberLength) / 2)

numberWords = num2words(totalPay, to="currency").upper() + " " + "* " * emptySpaces
numberWords = numberWords.replace("EURO,", "DOLLAR(S) AND")

paycheck.setTextAnchor("sw")
paycheck.setTextFont("times", "normal", 12)
paycheck.drawText(30, 185, numberWords)

# pay to the order of

paycheck.setTextJustify("left")
paycheck.setTextAnchor("nw")
paycheck.setTextFont("arial", "normal", 14)
paycheck.drawText(20, 200, "PAY TO THE\n"
                           "ORDER OF")

paycheck.setTextFont("times", "bold", 14)
paycheck.drawText(120, 200, employeeName.upper() + "\n")
paycheck.setTextFont("times", "italic", 16)
paycheck.drawText(120, 220, "1234 Street. \n"
                            "City, CA 12345 \n")

# signature
paycheck.setTextFont("times", "bold", 16)
paycheck.drawText(440, 230, "SIGNATURE")

paycheck.setTextFont("times", "bold italic", 35)
paycheck.drawText(580, 210, "paychecker")
paycheck.drawLine(550, 255, 760, 255)

print("Opened in new window...")

win.wait()

print("Thank You. Bye Bye")

"""
Sample Run:
Enter employee's name: Jason Chen
Enter employee's hourly wage as a decimal (ie. 2.20 for $2.20): 25.12
Enter employee's hours worked last week: 55
Processing information....
Printing Paycheck.....
Opened in new window...
Thank You. Bye Bye
"""