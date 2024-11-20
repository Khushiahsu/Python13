#Write a program to set screen size, colour for turtle graphics and draw a polygon using turtle?

import turtle

turtle.Screen().bgcolor("yellow")
turtle.Screen().setup(600,650)

polygon = turtle.Turtle()
sides = 6
side_length = 150
angle = 360.0/sides
for a in range(sides):
    polygon.forward(side_length)
    polygon.right(angle)

turtle.done()