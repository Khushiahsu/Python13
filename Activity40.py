#Write a program to draw a square inside a square?

import turtle

my_work=turtle.Screen()
my_work.bgcolor("cyan")
my_work.title("Spiral Activity")

squ1 = turtle.Turtle()
size = 0
while True:
    for squ2 in range(4):
        squ1.forward(size+1)
        squ1.left(90)
        size=size-5
    size=size+1

