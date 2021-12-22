#Practice Test 2 #6
x = 0
for i in range(10):
	for j in range(-1, -10, -1):
		x += 1
print(x)

print("/n")
#Practice Test 2 #13
nums = [1, 2, 3]
for i in range(len(nums)):
	nums.insert(i,i+1)
print(nums)


#Practice Test 2 #14
i = 0
while i > 3:
	i+=1
	print("Yes")
else:
	i -=1
	print("No")

print("/n")
#Practice Test 2 #14
def greeting(name= ""):
	print("Hello", name)
greeting()

print("/n")
#Practice Test 2 #20
def tripler(num):
	def doubler(num):
		return num *2
	num = doubler(num)
	return num * 3
print(tripler(2))

#Practice Test 2 #26
def myprint(*val):
	print(val)
myprint("Peter","Piper","Pickled","Pepper")


#Practice Test 2 #30
def fun(a = 3, b = 2):
	return b ** a
print(fun(2))


#Practice Test 2 #9
def func(num):
	while num > 0:
		nums = num - 1
num=3
func(num)
