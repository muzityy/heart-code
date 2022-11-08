import turtle

# set a window
wn = turtle.Screen()
wn.bgcolor("white")
wn.screensize(800, 600)

# set a pen
pen = turtle.Turtle()
pen.color("pink")
pen.shape("square")

# 画笔形状设成了非常可爱的海龟hh
pen.fillcolor("pink")
turtle.speed(200)


# define functions
def curve():
    for i in range(180):
        pen.right(1)
        pen.forward(2)


def heart():
    pen.left(135)
    pen.forward(720 / 3.14)
    curve()
    pen.left(90)
    curve()
    pen.forward(720 / 3.14)


def text():
    pen.penup()
    pen.setpos(-50, 50)
    pen.pendown()
    pen.color("white")
    pen.write('所有人暴富', font=("Verdana", 20, "bold"))


# painting!
pen.begin_fill()
pen.penup()
pen.setpos(0, -150)
pen.pendown()
heart()
pen.end_fill()
text()
turtle.done()