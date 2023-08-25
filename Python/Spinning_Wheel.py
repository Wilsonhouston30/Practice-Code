"""
Spinning wheel 
8/10 started


"""
import random
list_names = []
list_numbers = []
name = ""
attempts = -1
while name != "done":
    name = input("Enter the name: ")
    list_names.append(name)
    attempts += 1
    list_numbers.append(attempts)



# print(attempts)
list_names.pop()
# list_numbers.pop()
# print(list_names)
# print(list_numbers)
print()
for i in range(len(list_names)):
    index = list_names[i]
    print(f"{i} {index}")

print()
random_number = random.randrange(len(list_names))
print(f"{random_number}")
