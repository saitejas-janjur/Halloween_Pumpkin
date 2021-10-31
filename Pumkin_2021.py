import turtle

wn = turtle.Screen()
wn.bgcolor("black")

t=turtle.Turtle()
t.speed(8)
t.hideturtle()

def DrawCircle(x,y):
    t.color("Orangered")
    t.penup()
    t.goto(x, y)
    t.begin_fill()
    t.circle(150)
    t.end_fill()
DrawCircle(40,-100)
DrawCircle(-40,-100)

def Triangle(x, y):
    t.color("yellow")
    t.penup()
    t.goto(x,y)
    t.begin_fill()
    for i in range(3):
        t.forward(70)
        t.left(360/3)
    t.end_fill()
Triangle(40,80)
Triangle(-110,80)
Triangle(-30,15)

def Mouth():
    t.color("yellow")
    t.up()
    t.goto(-60,-20)
    t.down()
    t.begin_fill()
    t.goto(-30,-50)
    t.goto(30,-50)
    t.goto(60,-20)
    t.goto(0,-30)
    t.end_fill()
Mouth()

def Stem():
    t.color("green")
    t.up()
    t.goto(-40,195)
    t.down()
    t.begin_fill()
    t.goto(40,195)
    t.goto(20, 235)
    t.goto(10, 265)
    t.goto(0, 275)
    t.goto(-15, 255)
    t.goto(-10, 230)
    #t.goto(-15,140)
    # t.goto(-10,155)
    # t.goto(-40, 130)
    t.end_fill()
Stem()

turtle.Screen().exitonclick()

