
# Classes Challenges

# 1. Create a Rectangle class with attributes length and width. 
# Add methods to calculate the area and perimeter of the rectangle. 


# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
        
#     def area(self):
#         return self.length * self.width
    
#     def perimeter(self):
#         return 2 * (self.length + self.width)
    
    
# rect = Rectangle(5,10)
# print(rect.area())
# print(rect.perimeter())


# 2. Create a BankAccount class with attributes account_number and balance. 
# Add methods to deposit and withdraw money from the account. 


class BankAccount:
    def __init__(self, account_number, balance, amount):
        self.account_number = account_number
        self.balance = balance
        self.amount = amount
        self.deposittotal = balance + amount
        self.withdrawtotal = balance - amount
        
    def deposit(self):
        return self.account_number, self.balance, self.deposittotal
        
    def withdraw(self):
        return self.account_number, self.balance, self.withdrawtotal
        
bal = BankAccount(52342, 52302, 40000)
print(bal.deposit())    
print(bal.withdraw())


# 3. Create a Car class with attributes make, model, and year. 
# Add methods to get and set the values of the attributes. 

class Car:
    def __init__(self, make, model, year):
        self.make = str(make)
        self.model = str(model)
        self.year = str(year)
        self.full = make + " " + model + " " + str(year)
    def change_make(self):
        return self.make
        
    def change_make(self):
        return self.model 
        
    def change_make(self):
        return self.year
              
vehicle = Car("Hyundai", "Punto", 2013)
print(vehicle.make)
print(vehicle.model)
print(vehicle.year)
print(vehicle.full)


# 4. Create a Product class with attributes name, price, and quantity. 
# Add methods to calculate the total value of the product (price * quantity) 
# and add or remove items from the product inventory. 

# Part 1
# Create a Student class that takes the name and age on creation.
# Create 2 objects of your student class and get the age of one of them.

# Part 2
# With your Student class, make modifications for the class to accept the student’s current class (as in a classroom) on creation.
# Then add a method that takes 3 test scores and calculates the student’s average test   score.

# Part 3
# Create 3 classes, A bird parent class and then an Owl and Dodo class.
# Make use of the 4 OOP Principles.
