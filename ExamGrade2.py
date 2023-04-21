
# ExamGrade2.py created by AM on 21/04/2023
    
# Task 3 - ask for level and grade and base result on different values
# Error checks between 1-100

level = int(input("Please enter the students level: "))
grade = int(input("Please enter the students grade: "))


if(level==1):    
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
    
if(level==2):    
    if grade >= 66 and grade <= 100:
        print("Distinction")
    elif grade >= 51 and grade <= 65:
        print("Merit")
    elif grade >= 40 and grade <= 50:
        print("Pass")
    elif grade >= 1 and grade < 40:
        print("Fail")
    else:
        print("Error: marks must be between 1 and 100") 