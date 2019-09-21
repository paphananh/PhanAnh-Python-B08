from turtle import*
n = int(input ("How many?"))

a = (180*(n-2))/n

for i in range(n):
    left(180-a)
    forward(1)
