import turtle as t

from itertools import cycle
colors = cycle(['red', 'orange','yellow','green','blue','purple'])

def draw_circle(size):
    t.bgcolor(next(colors))
    t.pencolor('red')
    t.circle(size)
    draw_circle(size+5)

t.bgcolor('black')
t.speed('fast')
t.pensize(4)
draw_circle(30)
