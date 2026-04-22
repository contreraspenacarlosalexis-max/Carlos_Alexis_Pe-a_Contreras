#carlos alexis peña contreras
import turtle

t = turtle.Turtle()
t.speed(0)

colors = ["red", "blue", "green", "yellow", "purple"]

for i in range(50):
    t.color(colors[i % 5])
    for j in range(4):
        t.forward(100)
        t.right(90)
    t.right(10)

turtle.done()