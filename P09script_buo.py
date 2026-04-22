#carlos alexis peña contreras
import turtle

t = turtle.Turtle()
t.speed(5)
t.pensize(2)

# Función para mover
def mover(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# Fondo opcional
turtle.bgcolor("skyblue")

# Cuerpo
mover(0, -120)
t.color("brown")
t.begin_fill()
t.circle(100)
t.end_fill()

# Ojo izquierdo
mover(-40, 40)
t.color("white")
t.begin_fill()
t.circle(30)
t.end_fill()

# Ojo derecho
mover(40, 40)
t.begin_fill()
t.circle(30)
t.end_fill()

# Pupilas
mover(-40, 55)
t.color("black")
t.begin_fill()
t.circle(10)
t.end_fill()

mover(40, 55)
t.begin_fill()
t.circle(10)
t.end_fill()

# Pico
mover(0, 20)
t.color("orange")
t.begin_fill()
t.setheading(-60)
t.forward(20)
t.left(120)
t.forward(20)
t.left(120)
t.forward(20)
t.end_fill()

# Alas
mover(-100, -20)
t.color("darkred")
t.begin_fill()
t.setheading(-60)
t.circle(60, 120)
t.goto(-100, -20)
t.end_fill()

mover(100, -20)
t.begin_fill()
t.setheading(-120)
t.circle(-60, 120)
t.goto(100, -20)
t.end_fill()

# Orejas
mover(-50, 120)
t.color("brown")
t.setheading(60)
t.begin_fill()
t.forward(40)
t.right(120)
t.forward(20)
t.right(120)
t.forward(40)
t.end_fill()

mover(50, 120)
t.setheading(120)
t.begin_fill()
t.forward(40)
t.left(120)
t.forward(20)
t.left(120)
t.forward(40)
t.end_fill()

turtle.done()