# Code with Kartik



# All Rights Reserved


   
# Code Starts Here

import turtle

tu = turtle.Turtle()

tu.screen.bgcolor('black')

tu.pensize(2)

tu.color('red')

tu.left(90)

tu.backward(100)

tu.speed(500)

def tree (i):

    if i<10:

        return
    
    else:

        tu.forward(i)

        tu.color('white')

        tu.circle(2)

        tu.color('pink')

        tu.left(30)

        tree(3*i/4)

        tu.right(60)

        tree(3*i/4)

        tu.left(30)

        tu.backward(i)

tree(100)

turtle.done()

# Code Ends Here
