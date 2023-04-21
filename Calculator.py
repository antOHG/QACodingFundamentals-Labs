
# Calculator.py created by AM on 21/04/2023

def calculator():
    while True:
        # Print options for the user
        print("Enter '+' to add two numbers together")
        print("Enter '-' to subtract two numbers")
        print("Enter '*' to multiply two numbers")
        print("Enter '/' to divide two numbers")
        print("Enter 's' to find the squared number")
        print("Enter 'quit' to end the program")
        
        # Get user input
        user_input = input(": ")

        # Check if the user wants to quit
        if user_input == "quit":
            break
        # Check if the user input is a valid operator
        elif user_input in ["+", "-", "*", "/","s"]:
            
            # Get first number
            num1 = float(input("Enter a number: "))
            # Get second number
            num2 = float(input("Enter second number: "))

            # Calculate user_input
            if user_input == "+":
                result = num1 + num2
                print(num1, "+", num2, "=", result)

            elif user_input == "-":
                result = num1 - num2
                print(num1, "-", num2, "=", result)

            elif user_input == "*":
                result = num1 * num2
                print(num1, "*", num2, "=", result)

            elif user_input == "/":
                result = num1 / num2
                print(num1, "/", num2, "=", result)
                
            elif user_input == "s":
                result = num1 **2, num2 **2
                print(num1, "s", num2, "=", result)
        else:
            # Else show invalid input
            print("Invalid Input")

# Call the calculator function to start the program
calculator()