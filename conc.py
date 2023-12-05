'''palavra = 'boa tarde!'
print(palavra, len(palavra))

palavra = palavra + 'boa noite!'
print(palavra, len(palavra))

primeiro = '100'
segundo = '200'
print(primeiro + segundo)
print(primeiro * 3)
print(segundo * 3)


from calendar import *
year = int(input("Entre com o ano: "))
print(calendar(year))


import random

def cointoss():
    rand_i = random.randint(a: 0, b: 1)
    outcomes = ['cara', 'coroa']
    return outcomes[rand_i]

t1 = cointoss()
print(t1)'''

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