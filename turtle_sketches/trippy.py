import turtle
import random
import os
import canvasvg
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM


def draw(dir, name):
    turtle.hideturtle()
    polygon = turtle.Turtle()

    screen = turtle.Screen()
    turtle.bgcolor("black")
    polygon.speed(0)
    polygon.hideturtle()
    turtle.colormode(255)

    x = 0.01
    a = 0
    b = 0
    c = 255
    change_dir = 0
    for j in range(1000):
        if j >= 765:
            i = j - 765
        else:
            i=j
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

        polygon.circle(10+x*10)

        if change_dir == 0:
            polygon.forward(1+x)
        else:
            polygon.backward(1)
            polygon.backward(1)
        if j % 10 == 0:
            polygon.rt(90)


        x += 0.01
    polygon.hideturtle()

    nameSav = os.path.join(dir,"{}.svg".format(name))
    polygon.hideturtle()
    ts = turtle.getscreen().getcanvas()
    polygon.hideturtle()
    canvasvg.saveall(nameSav, ts)

    drawing = svg2rlg(os.path.join(dir,"{}.svg".format(name)))
    renderPM.drawToFile(drawing, os.path.join(dir,"{}.png".format(name)), fmt="PNG")


dir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "results")
draw(dir, "prova_trippy")

