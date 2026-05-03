# 1) Import the `turtle` module:
#    a) This module is used for drawing shapes on the screen.
import turtle
# 2) Set up the turtle screen:
#    a) Create a screen using `turtle.Screen()`.
#    b) Set the background color (example: "Orange").
turtle.Screen().bgcolor("red")
# 3) Create a turtle object for drawing:
#    a) Create a turtle (pen) using `turtle.Turtle()`.
#    b) Store it in a variable (example: `board`).
board = turtle.Turtle()
# 4) Draw the first triangle (part of the star):
#    a) Move forward to draw the base line.
#    b) Turn left by 120 degrees and draw the next side.
#    c) Turn left by 120 degrees again and draw the final side.
#    d) This completes the first triangle.
board.forward(100)
board.left(120)
board.forward(100)
board.left(120)
board.forward(100)
# 5) Move the turtle without drawing to reposition:
#    a) Lift the pen using `penup()`.
#    b) Turn the turtle slightly (example: right by 150 degrees).
#    c) Move forward to reach the new starting point.
board.penup()
board.right(150)
board.forward(50)

# 6) Draw the second triangle (to complete the star shape):
#    a) Put the pen down using `pendown()`.
#    b) Turn right to face the correct direction.
#    c) Draw three sides again:
#       - Move forward
#       - Turn by 120 degrees
#       - Move forward
#       - Turn by 120 degrees
#       - Move forward
#    d) This overlaps with the first triangle to form a star.
board.pendown()
board.right(90)
board.forward(100)
board.right(120)
board.forward(100)
board.right(120)
board.forward(100)
# 7) Keep the turtle window open:
#    a) Use `turtle.done()` so the drawing stays on screen.
turtle.done()