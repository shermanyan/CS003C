"""
Sherman Yan
Assignment 2 - P2.30
I:  none
P:  Generate Olympic Rings using ezgraphics
O:  Olympic Rings
"""
from ezgraphics import *

# set the center line of the canvas
xCenter = 250
yCenter = 150

win = GraphicsWindow(xCenter * 2, yCenter * 2)
canvas = win.canvas()

# ring size
ringSize = 100

# set line thickness for the rings
canvas.setLineWidth(6)

# rings from center
rowSpacing = 28

# blue ring
canvas.setOutline("dodgerblue3")
canvas.drawOval(xCenter - ringSize/2 - ringSize - 6, yCenter - ringSize / 2 - rowSpacing, ringSize, ringSize)

# black ring
canvas.setOutline("black")
canvas.drawOval(xCenter - ringSize/2, yCenter - ringSize / 2 - rowSpacing, ringSize, ringSize)

# red ring
canvas.setOutline("red3")
canvas.drawOval(xCenter + ringSize/2 + 6, yCenter - ringSize / 2 - rowSpacing, ringSize, ringSize)

# yellow ring
canvas.setOutline("gold")
canvas.drawOval(xCenter - ringSize - 3, yCenter - ringSize / 2 + rowSpacing, ringSize, ringSize)

# green ring
canvas.setOutline("chartreuse3")
canvas.drawOval(xCenter + 3, yCenter - ringSize / 2 + rowSpacing, ringSize, ringSize)

win.wait()

"""
Sample Code
- none
"""