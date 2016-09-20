#-------------------------------------------------------------------------------
# Name:     РћРєСЂСѓР¶РЅРѕСЃС‚Рё
# Purpose:

#
# Author:      Р§РµСЂРЅСЏРµРІ Р’Р°Р»РµРЅС‚РёРЅ
#
# Created:     20.09.2016
# Copyright:   (c) Р§РµСЂРЅСЏРµРІ Р’Р°Р»РµРЅС‚РёРЅ 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
n=int(input())

import turtle as t
t.speed(2)
t.right(90)
t.penup()
t.pendown()
for i in range (1, n+1):
    t.shape("turtle")
    t.circle(30*i, 360)
    t.circle(-30*i, 360)
t.mainloop()
done()