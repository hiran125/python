import turtle
turtle.speed(0)
turtle.bgcolor("black")
for i in range(5):
    for colours in {"red","magenta","blue","cyan","green","yellow","white"}:
        turtle.color(colours)
        turtle.pensize(3)
        turtle.left(20)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
