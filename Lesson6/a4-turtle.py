import turtle

# Set up screen
screen = turtle.Screen()
screen.bgcolor("lightblue")

# Create turtle
my_turtle = turtle.Turtle()
my_turtle.speed(3)
my_turtle.pensize(3)

# ---------------- TRIANGLE ----------------
my_turtle.penup()
my_turtle.goto(-250, 0)
my_turtle.pendown()

my_turtle.color("black", "red")
my_turtle.begin_fill()

for _ in range(3):
    my_turtle.forward(100)
    my_turtle.left(120)

my_turtle.end_fill()

# ---------------- RECTANGLE ----------------
my_turtle.penup()
my_turtle.goto(-50, 0)
my_turtle.pendown()

my_turtle.color("black", "green")
my_turtle.begin_fill()

for _ in range(2):
    my_turtle.forward(150)
    my_turtle.left(90)
    my_turtle.forward(80)
    my_turtle.left(90)

my_turtle.end_fill()

# ---------------- HEXAGON ----------------
my_turtle.penup()
my_turtle.goto(180, 0)
my_turtle.pendown()

my_turtle.color("black", "yellow")
my_turtle.begin_fill()

for _ in range(6):
    my_turtle.forward(80)
    my_turtle.left(60)

my_turtle.end_fill()

# Finish
turtle.done()