#Practice Exam 10 #10



#Practice Exam 10 #19
def funA(a):
	return a
def funB(b):
	return b * 2
def funC(c):
	return c + 3
x = funA(funB(funC(1)))
print(x)


#Practice Exam 10 #21
stuff = [
	["aa", "bbb", "c", "d"],
	["eeeee", "ff"],
]
biggest = ""
for i in stuff:
	for j in i:
		biggest = biggest if len(biggest) > len(j) else j
		print(i)
		print(j)
		print(biggest)
print(biggest)


#Practice Exam 10 #5
#dress = ("sock", "shirt", "hat")
#dress[0] = "pants"
#print(dress)
