#Practice Test 5 #18
cities = {"UK":"London","France":"Paris","Germany":"Berlin"}
for city in cities.items():
	print(city)
for country,city in cities.items():
	print(country,city)

#Practice Test 5 #19
a = 7
if a % 2 != 0:
	print("Got You!")
elif a > 4:
	print("hi")
else:
	print("bye")

#Practice Test 5 #21
for i in range(1, 3):
	print(i)
else:
	print("hi")


#Practice Test 5 #23
i = 0
while i < 4:
	i += 1
	print(i)
	break
else:
	print("Break")
	
print("\n")
#Practice Test 5 #24
i = 0
while i < 4:
	i += 1
	print(i)
else:
	print("Break")


print("\n")
#Practice Test 5 #25
def fun(x = 4, y = 5):
	y -= 1
	return x * y * 1
print(fun())


print("\n")
#Practice Test 5 #28
def fact(num):
	if num == 1:
		return 1
	return fact(num-1)*num
print(fact(4))


print("\n")
#Practice Test 5 #30
def fun(**names):
	for key, value in names.items():
		print(key, value, end=" ", sep=":")
fun(NAME="Robert",AGE=29, CITY="Dar es salaam")


print("\n")
for i in range(1, 4):
	print(i)
	break
else:
	print("hi")
	
i = 0
while i < 4:
	i += 1
	print(i)
	break
else:
	print("Break")
