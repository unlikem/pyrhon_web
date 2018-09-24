import turtle
turtle.setup(650, 650)
turtle.pensize(12)
turtle.pencolor("purple")
angle = 360 / 6
turtle.fd(100)
for i in range(5):
    turtle.left(angle)
    turtle.fd(100)
turtle.done()