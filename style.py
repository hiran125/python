import turtle
turtle.bgcolor("Black")



turtle.speed(0)
turtle.pensize(4)
turtle.pencolor("yellow")


def drawcircle (radius):
    for i in range (6):
        turtle.circle(radius)
        radius=radius-5

def drawdeaign():
    for i in range(9):
        drawcircle(100)
        turtle.right(50)

drawdeaign()
turrtle.done()
