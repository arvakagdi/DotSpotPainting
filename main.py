import turtle as t
import random

tim = t.Turtle()
tim.shape('turtle')
tim.pensize(15)
tim.speed('fastest')
t.colormode(255)

def randomColor():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    return (r,g,b)

directions= [0,90,180,270]

for _ in range(200):
    tim.forward(40)
    tim.color(randomColor())
    tim.setheading(random.choice(directions))



screen = t.Screen()
screen.exitonclick()