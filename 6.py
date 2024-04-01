from turtle import *

up()
tracer(150)
n = 25
for i in range(-10, 30):
    for j in range(-20, 30):
        goto(i * n, j * n)
        dot(3)
goto(-25, -25)
left(90)
down()
tracer(5)
for i in range(10):
    forward(15 * n)
    right(60)
done()