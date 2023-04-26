

# Classes and method is part of OOP - object orientated programming
# Key concepts:
# Class - a blueprint of attributes(variables), and methods (functions)
# we can use \ to make objects of a class
# Object - is an instance of a class
# Methods - Functions attached to a class
# Allows us to easily make multiple objects of the same type
# If we model a group of students if we didnt use classes we would need \
# to assign unique variables for each student

class Dog: # Creates a class called dog
    energy = "high" # setting an attribute for the class
    
    def speak(self): # Create method called speak (like a function)
        print("bark")
        
fido = Dog() # sets fido as an object of the class

# Redefine attribute

# fido.energy = "low"

print(fido.energy) # Calling the attribute
fido.speak() # Calling the method

###

class Students:
    pass

student_1 = Students()
student_2 = Students()

print(student_1) # Returns it is an object of the class Students and it's memory location

student_1.first = "joe"
student_1.last = "bloggs"
student_1.age = 18

print(student_1.first, student_1.last, student_1.age)

student_2.first = "jojo"
student_2.last = "basda"
student_2.age = 28

print(student_2.first, student_2.last, student_2.age)

# What if we needed to do this for 30 students?

class Student:
    def __init__(self, first, last, age): # __WORD__ indicates a background task
        self.first = first # Init initialises the object with these attributes
        self.last = last   # Self parameter refers to the object itself
        self.age = age     # The object itself is parsed as the first arguement
                           # Self maps the class data to the object data

student_3 = Student("john3", "smith", 10)
student_4 = Student("jj4", "smith", 11)


class Student1:
    def __init__(self, first, last, age):
        self.first = first 
        self.last = last   
        self.age = age    
        self.full = first + " " + last
        
student_5 = Student1("john5", "Smith", 13)
student_6 = Student1("jj6", "Smith", 12)

print(student_6.full)

# As a method..

class Student2:
    def __init__(self, first, last, age):
        self.first = first 
        self.last = last   
        self.age = age    
    
    def fullname(self):
        return(self.first  + " " + self.last)
        
student_7 = Student2("john7", "Smith", 14)
student_8 = Student2("jj8", "Smith", 15)

print(student_7.fullname())
print(Student2.fullname(student_8)) # same result as line 90

# Change an attribute with a method:

class Student3:
    def __init__(self, first, last, age):
        self.first = first 
        self.last = last   
        self.age = age    
    
    def fullname(self):
        return(self.first  + " " + self.last)
    
    def change_age(self):
        self.age = int(self.age + 1)

student_9 = Student3("john9", "Smith", 15)
student_10 = Student3("jj9", "Smith", 16)

print(student_9.age)
student_9.change_age()
print(student_9.age)

# Using a self-class variable

class Student4:
    
    age_increase_amount = 25 # self class variable
    
    def __init__(self, first, last, age):
        self.first = first 
        self.last = last   
        self.age = age    
    
    def fullname(self):
        return(self.first  + " " + self.last)
    
    def change_age(self):
        self.age = int(self.age + self.age_increase_amount)

student_11 = Student4("john9", "Smith", 15)
student_12 = Student4("jj9", "Smith", 16)

student_11.change_age()
print(student_11.age)


print(student_11.age_increase_amount) # returns the value of the variable from the object
print(Student4.age_increase_amount) # returns the class itself

#__dict__ dictionary from memory

print(Student4.__dict__)
print(student_11.__dict__)

Student4.age_increase_amount = 20
student_12.age_increase_amount = 15

print(Student4.age_increase_amount)
print(student_11.age_increase_amount)
print(student_12.age_increase_amount)


print(student_11.__dict__)
print(student_12.__dict__)

# Non self class variable

class Student5:
    
    age_increase_amount = 25 # self class variable
    num_of_students = 0
    
    def __init__(self, first, last, age):
        self.first = first 
        self.last = last   
        self.age = age    
    
        Student5.num_of_students += 1
    
    def fullname(self):
        return(self.first  + " " + self.last)
    
    def change_age(self):
        self.age = int(self.age + self.age_increase_amount)

student_13 = Student5("john9", "Smith", 13)
student_14 = Student5("jj9", "Smith", 14)

print(Student5.num_of_students)

# Parent class

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def eat(self):
        print(f"{self.name} is eating")
        
class Cat1(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed

    def meow(self):
        print("meow")
        def __str__(self):
            return f"{self.name}, ({self.species}, {self.breed})"
        
my_cat1 = Cat1("Whiskers", "feline", "Siamese")
my_cat1.meow()
my_cat1.eat()

print(my_cat1)


# Leading and trailing underscores
# _money = 100 - single leading underscore signifies is private.
# type_ print_ class_ -  single trailing underscore used for python keywords
# double leading underscore - name mangling - avoid collisions if our class is extended
# attribute not accessible without referring our class name
# we access them _classname__attributeName
