# Звезда
# Алгоритм https://sites.google.com/site/logomiry3/4
#

# Импорт библиотеки
from turtle import *

n1=0.0

n=int(input("Ввведите максимальное количество лучей( не менее 3)"))

shape ('arrow')
screensize(800,800)
color('red', 'yellow')
pensize(1)
speed('fast')

begin_fill() # пробуем покрасить с заливкой



for i in range (0,n):
        forward (200) # длина отрезка
        left (360*4/n) # угол

end_fill() # хватит лить краску
done() # функция окончания рисования