#Exercise 3.4
guest=['Einstein','Newton','Aristotle']
print("Mr. "+guest[0]+", "+"you are cordially invited to Carlo's dinner tonight.")
print("Mr. "+guest[1]+", "+"you are cordially invited to Carlo's dinner tonight.")
print("Mr. "+guest[2]+", "+"you are cordially invited to Carlo's dinner tonight.")

#Exercise 3.5
popped_guest=guest.pop(2)
print(guest)
print(popped_guest)

guest.insert(2,'Gallileo')
print(guest)
print("Mr. "+guest[0]+", "+"you are cordially invited to Carlo's dinner tonight.")
print("Mr. "+guest[1]+", "+"you are cordially invited to Carlo's dinner tonight.")
print("Mr. "+guest[2]+", "+"you are cordially invited to Carlo's dinner tonight.")

#Exercise 3.6
print("I found a bigger dinner table! More people coming folks!")
guest.insert(0,'Archimedes')
print(guest)
guest.insert(2,'Bohr')
print(guest)
guest.append('Feynman')
print(guest)

print("Mr. "+guest[0]+", "+"you are cordially invited to Carlo's dinner tonight.")
print("Mr. "+guest[1]+", "+"you are cordially invited to Carlo's dinner tonight.")
print("Mr. "+guest[2]+", "+"you are cordially invited to Carlo's dinner tonight.")
print("Mr. "+guest[3]+", "+"you are cordially invited to Carlo's dinner tonight.")
print("Mr. "+guest[4]+", "+"you are cordially invited to Carlo's dinner tonight.")
print("Mr. "+guest[5]+", "+"you are cordially invited to Carlo's dinner tonight.")


#Exercise 3.7
print("It is with great sadness that the bigger table cannot make it on time so I am inviting only two people for now")
popped_guest=guest.pop(0)
print(guest)
print(popped_guest)
print("Sorry Mr. "+popped_guest+ " I cannot invite you to dinner")
popped_guest=guest.pop(1)
print(guest)
print(popped_guest)
print("Sorry Mr. "+popped_guest+ " I cannot invite you to dinner")
popped_guest=guest.pop(2)
print(guest)
print(popped_guest)
print("Sorry Mr. "+popped_guest+ " I cannot invite you to dinner")
popped_guest=guest.pop(2)
print(guest)
print(popped_guest)
print("Sorry Mr. "+popped_guest+ " I cannot invite you to dinner")
print("Mr. "+guest[0]+", "+"you are still invited to Carlo's dinner tonight.")
print("Mr. "+guest[1]+", "+"you are still invited to Carlo's dinner tonight.")
print(guest)
del guest[0]
print(guest)
del guest[0]
print(guest)
len(guest)



