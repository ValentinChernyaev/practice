#Спираль

# Импорт библиотеки
from turtle import *



n=int(input("Ввведите число витков спирали (не более 10)"))

shape ('arrow')
screensize(800,800)
color('red', 'red')
pensize(3)
speed('fast')

begin_fill()
penup()
setposition(380, 380)
pendown()
for i in range(0,2*n) : # всего нужно 2*n секций
    for j in range(1,3): # фрагмент спирали из 3 секций
        backward (400-20*i)
        left(90)



done()