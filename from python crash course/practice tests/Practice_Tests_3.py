#Practice Test 3 #1
def func1() :
	print("func1")
	def func2():
		print("func3")
		def func3():
			print("func3")
		func3()
	func2()
func1()

print("\n")
#Practice Test 3 #3
for i in range(10,12,2):
	if i % 2 != 1:
		print("No")
else:
	print("Yes")

#Practice Test 3 #5
def fun(*val):
	print(type(val))
lst=[1,2,3,4,5]
number = 400
fun(lst,number)

def fun(*val):
	print(type(val))
lst={1,2,3,4,5}
number = 400
fun(lst,number)

print("\n")
greeting = "Good Morning"
for ch in greeting:
	if ch == 'o':
		break		
	print(ch)
else:
	print("Good Night")

print("\n")
#Practice Test 3 #16
if not(True):
	print("hi")
else:
	print("bye")

print("Hello","World")
print("Hello" "World")
print("Hello","World", end=" ")
print("Python")

print("Hello" "World", end=" ")
print("Python")

print("\n")
#Practice Test 3 #22
fruits = ["apples","bananas"]
for i in range(1,2):
	for fruit in fruits:
		print(i, fruit)

#Practice Test 3 #5
def fun(*val):
	print(type(val))
lst=[1,2,3,4,5]
number = 400
fun(lst,number)

print("\n")
#Practice Test 3 #27
a = 'Python'
i = 0
while i < len(a):
	i += 1
print(i)


#Practice Test 3 #28
def func(x):
	x = [1,2,3]
	return x
x = [4,5,6,7]
y = func(x)
print(x, y)

#Practice Test 3 #29
def area_square(side):
	return side ** 2
print(area_square(10))
