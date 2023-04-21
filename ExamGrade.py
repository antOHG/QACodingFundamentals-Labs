
# ExamGrade.py created by AM on 21/04/2023

# Task 2 - ask for an input from a user for a grade/mark
# Error checks between 1-100


grade = int(input("Please enter the grade: "))

if grade >= 71 and grade <= 100:
    print("Distinction")
elif grade >= 61 and grade <= 70:
    print("Merit")
elif grade >= 50 and grade <= 60:
    print("Pass")
elif grade >= 1 and grade < 50:
    print("Fail")
else:
    print("Error: marks must be between 1 and 100")
    
    