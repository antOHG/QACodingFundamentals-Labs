

# Classes Lab

# task 2

class Student:
    def __init__(self, name, age, class_="student"):
        self.name = name
        self.age = age
        self.class_ = class_

    def average_test_score(self, score1, score2, score3):
        x = (score1 + score2 + score3) / 300 * 100
        return f"{self.name} - average test score is {x}%"

student_1 = Student("person", 5)

print(student_1.average_test_score(20,60,60))


# task 3

class Bird:
    
    num_of_birds = 0
    
    def __init__(self, name, wingspan):
        self.name = name
        self.wingspan = wingspan
        
        Bird.num_of_birds += 1
    
    def fly(self):
        print(f"{self.name} is flying with a wingspan of {self.wingspan} cm")
    
    def __str__(self):
        return f"{self.name} ({self.__class__.__name__})"

class Owl(Bird):
    def __init__(self, name, wingspan, nocturnal=True):
        super().__init__(name, wingspan)
        self.nocturnal = nocturnal
        
    def hoot(self):
        print(f"{self.name} is hooting")

    def __str__(self):
        return super().__str__ + f" - nocturnal: {self.nocturnal}"
    
class Dodo(Bird):
    def __init__(self, name, wingspan, exctinct=True):
        super().__init__(name, wingspan)
        self.exctinct = exctinct
    
    def fly(self):
        print("Dodos cannot fly")
    
    def __str__(self):
        return super().__str__ + f" - exctinct: {self.exctinct}"        

bird1 = Bird("Eagle",20)
owl1= Owl("Barn owl", 90)
dodo1 = Dodo("The dodo",100)

bird1.fly()
print(bird1)

owl1.fly()
owl1.hoot()
print(owl1)

print(dodo1)
dodo1.fly()

print(Bird.num_of_birds)