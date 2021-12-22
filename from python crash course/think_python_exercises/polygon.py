import turtle
import math
bob = turtle.Turtle()
def polygon(t, n, length):
	angle = 360 / n
	for i in range(n):
		t.fd(length)
		t.lt(angle)
def circle(t, r):
	circumference = 2 * math.pi * r
	n = 50
	length = circumference / n
	polygon(t, n, length)
polygon(bob, 7, 70)
circle(10,10)
