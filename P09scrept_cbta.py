#carlos alexis peña contreras
import turtle

t = turtle.Turtle()
t.pensize(5)
t.speed(3)

def mover(x, y):
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()

# Letra C
mover(-200, 0)
t.circle(50, 180)

# Letra B
mover(-80, 0)
t.left(90)
t.forward(100)
t.right(90)
t.circle(-25, 180)
t.circle(-25, 180)

# Letra T
mover(40, 50)
t.setheading(0)
t.forward(100)
t.backward(50)
t.right(90)
t.forward(100)

# Letra A
mover(160, 0)
t.setheading(75)
t.forward(100)
t.right(150)
t.forward(100)
t.backward(40)
t.right(105)
t.forward(30)

turtle.done()