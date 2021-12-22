#Exercise 10.1
filename='learning_python.txt'
with open(filename) as file_object:
	words=file_object.readlines()
word_string = ''
for word in words:
	word_string += word.rstrip()
your_word = input("Enter what word you want to search: ")
if your_word in word_string:
	print("Your word appears in the learning_python.txt file")
else:
	print("Your word does not appear in learning_python.txt file")


#Exercise 10.2
filename='learning_python.txt'
with open(filename) as file_object:
	words=file_object.readlines()
word_string = ''
for word in words:
	word_string += word.rstrip()
your_word = input("Enter what word you want to search: ")
if your_word == 'Python':
	your_word.replace('Python','C')
	print("Your word appears in the learning_python.txt file")
else:
	print("Your word does not appear in learning_python.txt file")


