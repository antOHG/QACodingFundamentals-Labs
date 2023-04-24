

# Task 3 - TimeCalculator
# Timecalculator.py created by AM on 21/04/2023

def Timecalculator():
    from datetime import datetime
    while True:
        # Print options for the user
        print("Time Calculator")
        print("1- Add 2 date-times")
        print("2- Enter 'diff' to find the difference between 2 times")
        print("3- Enter 'ch' to convert to Hours")
        print("4- Enter 'cm' convert to Minutes")
        print("5- Enter 'mt' to convert Minutes to Time")
        print("6- Enter 'ht' to convert Hours to Time")
        print("7- Enter 'quit' to exit the program")
        
        # Get user input
        user_input = input("ENTER YOUR SELECTION: ")

        # Check if the user wants to quit
        if user_input == "1":
            while True:
                date_time1 = input("Enter time1 (in format DD:HH:MM): ")
                t1 = date_time1.split(':')
                if len(t1) == 3 and 0 <= int(t1[0]) < 24 and 0 <= int(t1[1]) and 0 <= int(t1[2] < 60):
                    break
                else:
                    print("Incorrect format of value")
            while True:
                date_time2 = input("Enter time2 (in format DD:HH:MM): ")
                t2 = date_time2.split(':')
                if len(t2) == 3 and 0 <= int(t2[0]) < 24 and 0 <= int(t2[1]) and 0 <= int(t2[2] < 60):
                    break
                else:
                    print("Incorrect format of value")
                    
        if user_input == "2":
            while True:
                date_time1 = input("Enter a datetime: ")
                t1 = date_time1.split(':')
                if len(t1) == 3 and 0 <= int(t1[0]) < 24 and 0 <= int(t1[1]) and 0 <= int(t1[2] < 60):
                    break
                else:
                    print("Incorrect format of value")
            while True:
                date_time2 = input("Enter a datetime: ")
                t2 = date_time2.split(':')
                if len(t2) == 3 and 0 <= int(t2[0]) < 24 and 0 <= int(t2[1]) and 0 <= int(t2[2] < 60):
                    break
                else:
                    print("Incorrect format of value")
            
        else:
            # Else show invalid input
            print("Invalid Input")

# Call the calculator function to start the program
Timecalculator()