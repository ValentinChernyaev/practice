#-------------------------------------------------------------------------------
# Name:        модуль1
# Purpose:
#
# Author:      Черняев Валентин
#
# Created:     20.09.2016
# Copyright:   (c) Черняев Валентин 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()