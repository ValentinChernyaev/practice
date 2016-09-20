
from turtle import *



n=int(input("Ввведите максимальное количество углов( не менее 3)"))

shape ('arrow')
screensize(800,800)
color('red')
pensize(3)
speed('fast')

begin_fill()
penup()
setposition(0, -380)
pendown()


for i in range (3,n+1):


 for j in range(0,i) :
        forward (200)
        left (360/i)


done()