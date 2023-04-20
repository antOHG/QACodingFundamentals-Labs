# - variables – a reference – the name of a variable
# - a section of memory
# - reserve memory and can’t be altered unless called by name

# - naming convention – should be descriptive, start with lower-case, not a number

# python3 vars+data_types.py
# person_one_age = 55   # snake_case
# personOneAge = 55     # CamelCase

#Var = # don’t use capital for variable of function
#1var = # don’t start with a number
#VAR = # not all caps either
#print = # cant use python keywords

# print(x) data displayed to standard output10

# type() data type of the variable
# input() user input text from standard input, defaults to string

# name = input("what is your name?: ")
# print("your name is" + " " + name)
# print(f"your name is {name}")
# print(type(name))

# age = input("age?: ")
# age1 = int(input("age?: "))
# print(type(age))
# print(type(age1))

# 4 main data types
# string- word, sentence, paragraph, str means string. Used to display info.
# Integers - a whole number
# float - decimal number
# boolean - True or False. Case Sensitive, equivalent 0 and 1

# string
# first_name = "steve"
# integer
# age - 32
# float
# wallet = 29.99

# name = "rex"
# age = 3
# bark = True
# meow = False

# print("Statement: ", name, "barks: ", bark)

# escape characters
# \\ backslash, \n new line, \t tab, \u or \U unicode, extended unicode

# print("my name is \"BOB\"")
# print("Person 1: \tHey, How are you?\nPerson 2: \tGood thanks! \U0001F604")

print("ASDAdasdaDSAD".lower())
print("hello world".upper())
print("hello world".replace("world", "class"))
print("hello world".count("o"))
print("hello world".split())
