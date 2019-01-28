import turtle
import random


t=turtle.Turtle()
wn = turtle.Screen()
wn.colormode(255)
wn.bgcolor(75,200,125)
t.shape('turtle')




def col():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    t.pencolor(r,g,b)


def squ():
    for i in range(4):
        col()
        t.forward(50)
        t.right(90)
    t.speed(0)
    
def sh():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    t.fillcolor(r,g,g)

def anyregPoly():
    for i in range(n):
        col()
        t.forward(100)
        t.left(360/n)
        sh()
        t.stamp()


n=12
anyregPoly()


