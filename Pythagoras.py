
# Pythagoras.py created by AM on 21/04/2023
    
# Task 4 - calculate the length of sides of triangle using Pythagoras Theorem
# Sqaure of the long side C of a right-angled triangle is the sum of the squares of
# the two shorter sides (A and B)
#  C**2 = A**2 + B**2


from math import sqrt

def PythagorasCalculator():
    while True:
        # Print options for the user
        print("Enter '1' to find the length of A given B and C")
        print("Enter '2' to find the length of B given A and C")
        print("Enter '3' to find the length of C given A and B")
        print("Enter 'quit' to end the program")

        # Get user input
        user_input = input(": ")

        # Check if the user wants to quit
        if user_input == "quit":
            break
        # Check if the user input is a valid operator
        elif user_input in ["1", "2", "3"]:

        # Get first number
            num1 = float(input("Enter a number: "))
        # Get second number
            num2 = float(input("Enter second number: "))
        
            if user_input == '1':
                side_a = int(input('Input the length of side a: '))
                side_b = int(input('Input the length of side b: '))
                side_c = sqrt(side_a * side_a + side_b * side_b)
                print('The length of side c is: ' )
                print(side_c)
            
            elif user_input == '2':
                side_b = int(input('Input the length of side b: '))
                side_c = int(input('Input the length of side c: '))
                side_a = sqrt((side_c * side_c) - (side_b * side_b))
                print('The length of side a is' )
                print(side_a)
                
            elif user_input == '3':
                side_a = int(input('Input the length of side a: '))
                side_b = int(input('Input the length of side c: '))
                side_c = sqrt(side_c * side_c - side_a * side_a)
                print('The length of side b is')
                print(side_c)
                
            else:
                print('Please select a side between a, b, c')
                
# Call the calculator function to start the program
PythagorasCalculator()