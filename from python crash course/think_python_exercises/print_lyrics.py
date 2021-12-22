def repeat_lyrics():
	print_lyrics()
	print_lyrics()
def print_lyrics():
	print("I'm a lumberjack, and I'm okay.")
	print("I sleep all night and I work all day.")
repeat_lyrics()


import turtle
bob = turtle.Turtle()
def square(t):
	for i in range(4):
		t.fd(100)
		t.lt(90)
square(bob)

word = 'banana'
count = 0
for letter in word:
	if letter == 'a':
		count = count + 1
print(count)
