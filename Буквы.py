﻿
from turtle import *

simvol=" "




simvol=input("Введите строку команд :") # считать через input()
print(simvol)

shape ('arrow')
screensize(800,800)
color('green')
pensize(3)
speed('slow')



for i in simvol:

   if i=='l': left(1)
   if i=='r': right(1)
   if i=='g': forward(1)



done()