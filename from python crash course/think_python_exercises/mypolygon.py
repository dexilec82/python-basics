#The Turtle module
import turtle
bob = turtle.Turtle()
print(bob)
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)
turtle.mainloop()

for i in range(4):
 print('Hello!')
 
for i in range(4):
 bob.fd(100)
 bob.lt(90)

import turtle
bob = turtle.Turtle()
def square(t):
	for i in range(4):
		t.fd(100)
		t.lt(90)
square(bob)
