#Practice Exam 9 #6
if False:
	print("Nissan")
elif True:
	print("Ford")
elif True:
	print("BMW")
else:
	print("Audi")

#Practice Exam 9 #23
def loud(sound,sounds):
	return f"{sound} is noisy"
print(loud("factory", "explosion"))

#Practice Exam 9 #24
result = 0
numbers = [2, 4, 6]
for num in numbers:
	result = result + num
print(num)
print(result)

#Practice Exam 9 #27
word = ""
counter = 0
letters = ["c", "a", "r"]
while counter < len(letters):
	word = word + letters[counter]
	counter = counter + 1
print(word)
