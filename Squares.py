
# Squares.py created by AM on 21/04/2023
    
# Chapter 03 Lab - Part 1
# Using while loops
# Task 1 - Squares
# incomplete


x = 0
while x <100:
    square = x**2
    if square > 2000:
        break
print(x, "=" + square)
x += 1
        
for x in range(1,101):
     square = x **2
     if square >2000:
        break
print(x, "=" + square)       
        
# task 2

num = int(input("Enter a number: "))
factorial = 1
while num > 1:
    factorial *= num # 1 * 5 = 5, 5* 4 = 20, 20 * 3 = 60, 60 * 2 = 120
    num -= 1
    print("Factorial: ", factorial)
    
# task 3
    
initial_investment = float(input("Initial investment: £"))
target_value = float(input("Target value: £"))
interest_rate = float(input("Interest rate percentage: %")) / 100.0

years = 0
while initial_investment < target_value:
    initial_investment *= (1+ interest_rate)
    years += 1
    print(f"It will take {years} to grow to £{target_value}.")

# task 4

min = 1
max = 100
tries = 0
while tries <3:
    value= int(input(f"Integer between {min} and {max}: "))
    if min <= max:
        print(f"valid value entered {value}")
        break
    else:
        print (f"Invalid value added {max}")
        

word = input("enter a word: ")
vowel_count = 0
counter = 0
while counter < len(word):
    x = word[counter]
    if x.lower() in "aeiou":
        vowel_count += 1
        counter += 1
        
print(f"number of vowels in '{word} is {vowel_count}")

# Task 6

maths = 999
english = 999
IT = 999
while (maths < 0 or maths >100):
    maths = int(input("Enter maths mark (0-100"))
while (english < 0 or english >100):
    english = int(input("enter english mark (0-100)"))
while (IT < 0 or IT >100):
    IT = int(input("enter IT mark (0-100)"))
    
average = (maths + english + IT) / 3

if average >= 65:
    reuslt = "pass"
else: result = "fail"

print(f"Average mark: {average}")
