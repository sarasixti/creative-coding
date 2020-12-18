import turtle
import random
import canvasvg
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM


def draw():
    polygon = turtle.Turtle()
    screen = turtle.Screen()

    polygon.hideturtle()
    turtle.colormode(255)
    for i in range(1000):

        change_color = random.randint(0,1)
        if change_color == 0:
            polygon.pencolor((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
            
        polygon.down()
        polygon.forward(random.randint(-100,100))
        polygon.right(90)
        polygon.forward(random.randint(-100,100))
        polygon.right(90)
        polygon.forward(random.randint(-100,100))
        polygon.right(90)
        polygon.forward(random.randint(-100,100))
        polygon.right(90)
    polygon.hideturtle()

    nameSav = "prova.svg"
    ts = turtle.getscreen().getcanvas()
    canvasvg.saveall(nameSav, ts)

    drawing = svg2rlg("prova.svg")
    renderPM.drawToFile(drawing, "prova.png", fmt="PNG")

draw()