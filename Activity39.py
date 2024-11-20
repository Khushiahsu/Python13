#Write a program to draw a star using a turtle?

import turtle

turtle.Screen().bgcolor("blue")
turtle.Screen().setup(700,775)

star = turtle.Turtle()
star.forward(200)
star.left(120)
star.forward(200)
star.left(120)
star.forward(200)
star.penup()
star.right(150)
star.forward(50)
star.pendown()
star.right(90)
star.forward(200)
star.right(120)
star.forward(200)
star.right(120)
star.forward(200)
star.right(120)
turtle.done()