import turtle
import random
import canvasvg
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM


def draw():
    turtle.hideturtle()
    polygon = turtle.Turtle()

    screen = turtle.Screen()
    turtle.bgcolor("black")
    polygon.speed(0)
    polygon.hideturtle()
    turtle.colormode(255)

    x = 0
    a = 0
    b = 0
    c = 255
    for i in range(1000):
        if i >= 765:
            i = i - 765
        if i < 255:
            polygon.pencolor(a, 0, c)
            a += 1
            c -= 1
        elif 255 <= i < 510:
            polygon.pencolor(a, b, 0)
            b += 1
            a -= 1
        else:
            polygon.pencolor(0, b, c)
            c += 1
            b -= 1
        polygon.fd(10+x)
        polygon.rt(90.7)
        x += 0.7
    polygon.hideturtle()

    nameSav = "prova.svg"
    polygon.hideturtle()
    ts = turtle.getscreen().getcanvas()
    polygon.hideturtle()
    canvasvg.saveall(nameSav, ts)

    drawing = svg2rlg("prova.svg")
    renderPM.drawToFile(drawing, "prova.png", fmt="PNG")


draw()