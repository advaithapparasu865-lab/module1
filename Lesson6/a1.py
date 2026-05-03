import turtle
turtle.Screen().bgcolor("blue")
turtle.Screen().setup, (400, 500)
polygon = turtle.Turtle()
num_sides = 4
angle = 90
for i in range (num_sides):
    polygon.forward(70)
    polygon.right(angle)
turtle.done()