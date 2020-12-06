import turtle as t
import random

tim = t.Turtle()
tim.shape('turtle')
tim.speed('fastest')
t.colormode(255)

def randomColor():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    return (r,g,b)

for _ in range(120):
    tim.color(randomColor())
    tim.circle(150)
    tim.right(3)




screen = t.Screen()
screen.exitonclick()