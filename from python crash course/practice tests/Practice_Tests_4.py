#Practice Test 4 #1
s = 0
for i in range(1, 10):
	s = s + i
	print(s)
print(s)

print("\n")
def func(mylist):
	mylist[3]="strawberries"
lst = ["bananas","apples","pears","peas"]
func(lst)
print(lst)


#Practice Test 4 #4
for i in range(1) :
	for j in range(1):
		print(i,j)

#Above example is an accumulator
"""
s=0
0+1 = 1

s=1
1+2 = 3

s=2
3+3 = 6

s=5
6+4 = 10

s=10
10+5 = 15

s=15
15+6 = 21

s=21
21+7 = 28

s=28
28+8 = 36

s=36
36+9 = 45
"""

print("\n")
#Practice Test 4 #9
a = 'python'
i = 0
while i < len(a):
	i += 1
	pass
print('Value of i :', i)


#Practice Test 4 #11
a = ["Monday", "Wednesday", "Thursday"]
a.insert(1,"Tuesday")
a.append("Friday")
print(a)

print("\n")
#Practice Test 4 #16
def fun(y,x=5):
	return x/y
print(fun(2))

print("\n")
#Practice Test 4 #17
temp = "True"
while not temp:
	print("Temp")
else:
	print("Fixed")

print("\n")
#Practice Test 4 #19
for i in range(3):
	print(i,end=" ")
print(i)


#Practice Test 4 #24
name = ""
while name:
	print("Good Morning")
else:
	print("Good Night")

#Practice Test 4 #13
def fun(data, *num ):
	print(data)
	print(num)
fun("Earth", 2, True, "Jupiter")


#Practice Test 4 #19
a = 7
if a % 2 != 0:
	print("got you")
elif a > 4:
	print("hi")
else:
	print("bye")
	
	
#Practice Test 4 #21
for i in range(1, 3):
	print(i)
else:
	print("hi")


#Practice Test 4 #22
for i in range(1, 4):
	print(i)
	break
else:
	print("hi")


#Practice Test 4 #23
i = 0
while i < 4:
	i += 1
	print(i)
	break
else:
	print("Break")


#Practice Test 4 #25
def fun(x = 4, y = 5):
	y -= 1
	return x * y * 1
print(fun())

#Practice Test 4 #28
def fact(num):
	if num == 1:
		return 1
	return fact(num-1)*num
print(fact(4))

#Practice Test 4 #30
def fun(**names):
	for key, value in names.items():
		print(key, value, end=" ", sep=":")
fun(NAME="Robert",AGE=29, CITY="Dar es salaam")

print("\n")

#Practice Test 4 #27
def fun(x):
	return["Tea"]
coffees = ["Cappuccino","Latte","Macchiato"]
tea = fun(coffees);
print(tea)
