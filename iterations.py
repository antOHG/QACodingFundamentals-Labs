
# Iterations

# Iterations is another word for loops, repeating a block of code over and over
# Without having to write the code multiple times, saving time

# 2 types of loops
# while loops
# For loops

# While loops
# A while loop  will continue to execute code while a condition is true
# if a condition is never true the while loop with never start

# print ("1")
# print ("2")
# print ("3")
# print ("4")
# print ("5")

# x = 0

# while x <100:
#     print(x)
#     x += 1 # same as x = x + 1
    
# break

# i = 1
# while i < 6:
#     if i == 3:
#         break
#     print(i)
#     i += 1
    
# # continue

# j = 6

# while j <6:
#     j += 1
#     if j == 3:
#         continue
#     print(j)
    
    

# k = 1
# while k < 6:
#     print(k)
#     k += 1
    
# else:
#     print("k is no longer less than 6")
    
    

# For loops
# A For loop will iterate over iterable collection - lists/strings/dictionaries
# useful for when we want to use data in collection
# Do things to individual elements in a collection

# iterating through lists

# numbers = [1, 3, 5, 9]

# for item in numbers:
#     print(item)
    
# l = 0 
# while l < len(numbers):
#     print(numbers[1])
#     l += 1
    
# # Make changes

# my_fruits = ["apple","orange","banana"]

# for fruit in my_fruits:
#     print(fruit.upper())
    
# # Range

# for a in range(5):
#     print(a) # 0-4 (stops at 5)

# for a in range(1,5):
#     print(a)  # 1-4
    
# for a in range(1,10, 2):
#     print(a)  # intervals/in steps of 2 (3rd argument)

# # strings
# for x in "hello":
#     print(x)
    
# for word in "hello world".split():
#     print(word)
    
# # List comprehension - find squared numbers

# result = [x**2 for x in range(5)]
# print(result)

# # same as 

# results = []
# for x in range(5):
#     results.append(x**2)
# print(results)

# # Dictionary iteration:

# for i in {"drink":"wine"}:
#     print(i)
    
# for value in {"food": "jam"}.values():
#     print(value)

# for key, value in {"shape":"square"}.items():
#     print(key+":", value)   
    

# # Break and continue

# for i in range(10):
#     if i == 5:
#         continue
#     print(i)
    
# for i in range(10):
#     print(i)
#     if i == 5:
#         break
    
    
# # nested loops:

# for i in range(100):
#     for j in range(100):
#         print(i, "x", j, "=", i*j)
        
        

# iterations.py created by AM on 21/04/2023

# Write a while loop which asks for the name of 5 people
# for each person print their name followed by the text "is great!"

counter = 0

names = input("Enter the names of 5 people")

while counter < 5:
    name = input("Please enter a name ")
    print(name + " is great!")
    counter += 1