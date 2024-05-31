# Code with Kartik



# All Rights Reserved



# Code Starts Here 

import turtle

screen = turtle.Screen()

screen.bgcolor("black")  # Set background color to black

t = turtle.Turtle()

t.speed(0) 

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

for i in range(360):

    t.color(colors[i % 7])

    t.width(i/100 + 1)      

    t.forward(i)

    t.left(59)

t.hideturtle()

turtle.done()

# Code Ends Here
