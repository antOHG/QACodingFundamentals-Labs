
# # # functions.py created by AM 25/04/2023

# # # Functions - a block of code that either performs a task or return a value
# # # Interchangable

# # def greet(name): # Parameter which takes arguement
# #     print(f"hi {name}")
    
# # greet("bob")

# # def greet1(first_name, second_name, age):
# #      print(f"{first_name} {second_name} is {age}")
           
# # greet1("joe", "bloggs", "18")

# # # More functionable to use 'return'. You can store in a variable, sent to file and print outside of the function. Useful if no access to command line through a web app for instance.
# # # Avoid input() - or anything that uses the command line

# # def greeter(name):
# #     return(f"hello {name}")

# # x = greeter("bob")

# # print(x)

# # def greet3(name, age=10): # default arguements must come as last arguements
# #     return(f"{name} is {age}")

# # print(greet3("John"))
# # print(greet3("John",20))


# def addCalculator(first_number, second_number):
#     x = first_number + second_number
#     return x

# print(addCalculator(5,5))

# # *args
# # If you do not know how many arguements will passed into your function
# # add a * before the parameter name
# # it will receive a tuple of arguments

# def fruit_list(*fruits):
#     print("the fruit are: ")
#     for fruit in fruits:
#         print(fruit)

# fruit_list("apple","orange","pear")

# def numbers_list(*numbers):
#     for i in numbers:
#         print(i)

# numbers_list(1,2,3,4,5, 6)

# # Keyword arguments - kwargs
# # send arguments as key-value pairs
# # we define the value when we pass the argument

# def fruit_list1(fruit1, fruit2, fruit3):
#     print(f"Most favourite = {fruit1}")
#     print(f"2nd favourite = {fruit2}")
#     print(f"Least favourite = {fruit3}")
    
# fruit_list1(fruit1 = "apple", fruit3 = "pear", fruit2 = "orange")
    
# # We alos have **kwargs
# # Used if we dont know how many keyword arguements there will be


# def fav_food(**food):
#     print("Favourite food is", food["fruit"], "not", food["dairy"])
    
# fav_food(dessert = "ice-cream", fruit = "blueberries", dairy = "cheese")

# Passing a list as an argument

def my_function(food):
    for x in food:
        print(x)
        
list1 = ["apple","banana", "cherry"]

my_function(list1)

# # format example - using {} as a placeholder
# name = "john"
# age = 20
# height = 1.7

# print("my name is {}, I am {}, my height is {}".format(name, age, height))
# # Also with a variable