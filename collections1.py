# # Different ways of storing data
# # lists - ordered, mutable, collection of values []
# # Dictionaries - unordered, mutable, collection of key-value pairs. {"key": "value", ...}
# # Tuples - ordered, immutable, collection of values ()
# # Sets - unordered, mutable, collection of unique values. {"value1", "value2, ....."}

# # lists - multiple values in a single variable. []

# colours = ["Blue","Red","Green","Yellow"]

# print(colours)


# # Referencing - elements in a list are referenced by their index position
# # starts from 0 or going backwards -1.

# print(colours[0])
# print(colours[-4])

# # slicing - create sub-list up to but not including the second number

# print(colours[0:2])
# print(colours[1:])

# # Altering - use index position, need new value, delete

# food = ["bread", "cheese","pasta","apple"]
# food[0] = "rice"
# del food[1]

# print(food)

# # checking if an item is in a list
# print("pasta" in food)
# print("orange" in food)

# # nested lists
# numbers = [1, 2, 3, 4]
# letters = ["a", "b", "c", "d"]

# combined = [numbers, letters]

# print(combined[0][1], combined[1][1])

# # multiple data types can be in lists
# my_list = ["red", 5, ["green", "apple"], 10.5]

# print(my_list)
# print(my_list[2][0])
# print(my_list[0])

# # list methods

# # append
# my_fruits= ["apple","orange","kiwi"]
# my_fruits.append("banana")
# print(my_fruits)

# # remove
# my_fruits.remove("orange")
# print(my_fruits)

# # insert
# my_fruits.insert(0,"pineapple")
# my_fruits.insert(1,"grapes")
# print(my_fruits)

# # extend
# my_fruits.extend(["mango","melon"])
# print(my_fruits)

# # find index
# print(my_fruits.index("mango"))

# # reverse
# my_fruits.reverse()
# print(my_fruits)

# # sort alphabetically
# my_fruits.sort()
# print(my_fruits)

# # sort by length
# my_fruits.sort(key=len)
# print(my_fruits)

# # join
# x = ", ".join(my_fruits)
# print(x)

# # Dictionaries : {} key-pair values
# # similar to list but no indexing
# # keys have to be unique, values dont.

# drinks = {"fizzy": "sprite","still": "water", "juice": "orange", "alcoholic": "beer"}
# print(drinks)
# print(drinks["still"]) # can only query keys not values
# print(drinks["fizzy"]) # can only query keys not values
# print(drinks["juice"]) # can only query keys not values
# print(drinks["alcoholic"]) # can only query keys not values

# # add to a dictionary
# drinks["non-alcoholic"] = "water"
# print(drinks)

# # Overwrite

# drinks["non-alcoholic"] = "squash"
# print(drinks) 

# # return all values or keys

# print(drinks.values())
# print(drinks.keys())
# print(drinks.items())

# print("water" in drinks.values())
# print("still" in drinks)

# # get method
# print(drinks.get("still", "not-found"))
# print(drinks.get("stille", "not-found"))
# print(drinks.get("stillle"))

# # update

# drinks.update({"sugary": "cola"})
# print(drinks)
# # or
# drinks.update(very_sugary = "red-bull")
# print(drinks)

# # pop
# print(drinks.pop("non-alcoholic"))
# print(drinks)

# print(drinks.pop("non-alcoholic", "not-found"))


# # dictionary exercise

# books = {"the handmaiden's tale": "margaret atwood", "the hobbit": "tolkien"}
# print(books["the handmaiden's tale"])

# Make a books dictionary with 3 authors as keys and multiples as values.
# Use an input() asking for author name and print as a string the list of books by that
# author. Use the .join() method


# books_dict = {"JK Rowling": ["Sorcerers Stone","Chamber of Secrets","Prisoner of Azkaban"],}

# y = input("Please enter author name: ")
# print(", ".join(books_dict[y]))


# tuples

# we cant change data in a tuple
# read only
# () instead of {} list, or nothing at all

# shapes = ("square", "circle", "triangle")
# shapes1 = "square", "circle","triangle"

# print(type(shapes))
# print(type(shapes1))

# shapes.append("rectangle")
# print(shapes)

# less memory to store data
# speed - slightly faster
# indicates that we dont want to change the data

# sets 
# no indexing
# no duplicate values + can't be nested
# {}

items = {"apple","banana","pear"}
print(type(items)) 