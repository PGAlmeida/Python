from itertools import cycle
from time import sleep

listas = [1, 2, 3, 4, 5]

while True:
    for lista in cycle(listas):
        print(lista)
        sleep(1)
    