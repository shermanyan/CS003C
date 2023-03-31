"""
Sherman Yan
Assignment 2 - P2.25
I:  none
P:  Generate a happy face using EZ Graphics
O:  Happy face
"""
from ezgraphics import *

win = GraphicsWindow(500, 500)
canvas = win.canvas()

# set line color and thickness for everything
canvas.setOutline("blue")
canvas.setLineWidth(2)

# circle for face
circleDiameter = 110
canvas.drawOval(250 - (circleDiameter/2), 250 - (circleDiameter/2), circleDiameter, circleDiameter)

# circle for eyes
eyeSize = 12
canvas.drawOval(230 - (eyeSize/2), 238 - (eyeSize/2), eyeSize, eyeSize)
canvas.drawOval(270 - (eyeSize/2), 238 - (eyeSize/2), eyeSize, eyeSize)

# mouth line
canvas.drawLine(220, 273, 280, 273)

win.wait()

"""
Sample Code
- none
"""