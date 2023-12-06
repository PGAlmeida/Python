'''
from turtle import *

bgcolor("black")
color("red")
title("StudyMuch")
begin_fill()
pensize(3)
left(50)
forward(133)
circle(50, 200)
right(140)
circle(50, 200)
forward(133)
end_fill()
done()


import turtle 
import colorsys

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(0)
n = 36
h = 0.5
for i in range(80):
    c = colorsys.hsv_to_rgb(h,1,1)
    h+=1/n
    t.color(c)
    t.left(5)
    for j in range(5):
        t.forward(250)
        t.left(144)



import turtle

animation = turtle.Turtle()
animation.speed(40)
animation.hideturtle()
animation.getscreen().bgcolor("black")
animation.color("aqua")

for i in range(170):
    animation.circle(i)
    animation._rotate(5)


from turtle import *
import colorsys

bgcolor("black")
width(2)
h = 0.0
for i in range(250):
    speed(18)
    c = colorsys.hsv_to_rgb(h,1,1)
    color(c)
    forward(i*2)
    right(121)
    h+=0.005

done()
'''

from turtle import *

color("green")
bgcolor("black")
speed(10)
hideturtle()
b = 0
while b < 200:
    right(b)
    forward(b * 3)
    b = b + 1