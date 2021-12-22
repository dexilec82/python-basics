#Practice Test 6 #4
x = 5
def fun(x):
	x = x - (x-2)
	return x
print(fun(fun(fun(x-1))))

#Practice Test 6 #6
count = 0
for i in range(0,2):
	for j in range(0,2):
		count+=1
print(count)

print("\n")
#Practice Test 6 #15
x=1
if x>0:
	print("*")
	if x<2:
		print("*")
	elif x==1:
		print("*")
	else:
		print("*")
else:
	print("*")

print("\n")
#Practice Test 6 #29
fruits = ["apples","cherries"]
for fruits[-1] in fruits :
	print(fruits[-1], end ="|")

print("\n")
#Practice Test 6 #14
lst = [x for x in range(3)]
print(lst)

lst = x 
for x in range(3):
	print(lst)
print(lst)


#Practice Test 6 #24
def add(new_value, values=[]):
	values.append(new_value)
	return values
vals = add("Toyota",["BMW","Mercedes"])
print(add("Ford", vals))


while True:
	name = input("What is your name?")
	if name == 'quit':
		print("Exit")
		break
	else:
		print("Hello, ", name)


fruits = ["apples","cherries"]
for fruits[-1] in fruits :
	print(fruits[-1], end ="|")
