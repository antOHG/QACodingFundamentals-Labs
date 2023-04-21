

# if, elif, else
# condtional statements are used to accomodate different paths our code may take
# we use if statements to run code if a given condition is met

# my_bool = False

# if my_bool:
#     print("my_bool is true")
# else:
#     print("my_bool is false")

# # nest if statements
# if some-condition:
#     if some other condition:
#         .....
#     else:
#         .....
# else:
#     .....
    
    
# Conditionals.py created by AM on 21/04/2023

# conditionals
# equals to: ==
# not equals to: !=
# less than: <
# more than: >
# less than or more than equals to: <= / >=

# exampels

# money = 1
# if money >10:
#     print("I'm rich!")
# else:
#     print("I'm poor!")
    
    
# elif - else if
# we don't always have to check if every statement equates to true
# Mostly only only one statement will be true/relevant
# elif makes our code more efficient
# will only run if no other statement has been evaluated as true

# temp = 2

# if temp >= 30:
#     print("It's a very hot day")
# elif temp >25:
#     print("It's hot")
# elif temp >20:
#     print("It's ok")
# elif temp >15:
#     print("Could be better")
# elif temp == 0:
#     print("It's freezing")
# else:
#     print("Bad weather")
    
    
# Exercise - ask for an input from a user for a grade/mark
# if the mark is greater than 85 print "Distinction"
# if the mark is between 65 and 85 "Pass"
# anything else print "Fail"
# if + elifs


# grade = int(input("Please enter the grade: "))

# if grade >= 85:
#     print("Distinction")
# elif grade >=65:
#     print("Pass")
# else:
#     print("Fail")
    
# multiple comparators + with mutliple conditions using and/or:

# deposit = 0
# password="password"

# # if 0 < deposit  <= 100 and password == "password":
# #     print(f"Thank you for £{deposit} deposit")
# # else: 
# #     print("Failed to deposit")

# if not(0 < deposit <= 100) or password != 'password':
#     print("Failed to deposit")
    
# else:
#     print(f"Thank you for your £{deposit} deposit")
    

# in and not in:

# name ="root"

# if name in("root", "admin","sa"):
#     print("Invalid username") 
# else:
#     print(f"Welcome {name}")
    
# name ="groot"

# if name not in("root", "admin","sa"):
#     print(f"Welcome {name}")
# else:
#     print("Invalid username") 
    
# Challenge:
# weight converter app, convert a user input weight (float) and user to select
# either Kgs or Lbs from a prompt. Write an if statement that checks if the units 
# entered is Kgs or Lbs. If Kgs convert into Lbs and print converted weight
# else to handle the other conversion. Error handling upper/lower case Kgs/kgs

weight=float(input("Enter your weight: "))
unit=input("Enter either Kgs/kgs or Lbs/lbs: ")

if unit.upper() in ("kgs"):
    weight = float(weight*2.20462)
    print (f"Your weight {weight} is in lbs")
else:
    weight = float(weight/2.20462)
    print (f"Your weight {weight} is in Kgs")
    
    
weight=float(input("Enter your weight: "))
unit=input("K (Kgs) or L (Lbs): ")

if unit.upper() == ("K"):
    converted = weight / 0.45 
    print (f"Your converted weight {converted} in Lbs")
else:
    converted = weight * 0.45
    print (f"Your converted weight {converted} in Kgs")