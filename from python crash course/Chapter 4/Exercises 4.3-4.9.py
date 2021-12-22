#Exercise 4.3
for number in range(1,21):
	print(number)

#Exercise 4.4-4.5
million=list (range(1,1000001))
print(million)
min(million)
max(million)
sum(million)

#Exercise 4.6
print("\n")
even_numbers=list(range(1,21,2))
print(even_numbers)

print("\n")
for odd_numbers in range(1,21,2):
	print(odd_numbers)

#Exercise 4.7
print("\n")
three_multiples=list (range(3,30,3))
print(three_multiples)

#Exercise 4.8
print("\n")
cube=[]
for value in range(1,10):
	cubes=value**3
	cube.append(cubes)
print(cube)

#Exercise 4.9
print("\n")
cubes=[value**3 for value in range(1,10)]
print(cubes)







