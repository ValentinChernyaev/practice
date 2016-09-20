
from turtle import *

n=int(input("Ввведите количество ног паука"))
shape ('circle')

color('black', 'black')
pensize(5)

begin_fill()

for i in range(1,n+1) :
    forward (200)
    stamp()
    backward(200)
    left(360/n)

end_fill()
done()