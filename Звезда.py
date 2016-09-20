
from turtle import *

n1=0.0

n=int(input("Ввведите максимальное количество лучей( не менее 3)"))

shape ('arrow')
screensize(800,800)
color('red', 'yellow')
pensize(1)
speed('fast')

begin_fill()



for i in range (0,n):
        forward (200)
        left (360*4/n)

end_fill()
done()