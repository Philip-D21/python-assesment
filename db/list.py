# Creating a list
fruits = ["apple", "banana", "orange", "grape"]

# Accessing elements in a list
first_fruit = fruits[0]
print("First fruit:", first_fruit)


# Modifying elements in a list
fruits[1] = "mango"

# Adding elements to a list
fruits.append("kiwi")

# Removing an element from a list
removed_fruit = fruits.pop(2)

# Iterating through a list
for fruit in fruits:
    print(fruit)

# List comprehension
squared_numbers = [x**2 for x in range(5)]

# Checking if an element is in the list
is_mango_in_list = "mango" in fruits

# Length of a list
num_fruits = len(fruits)

# Sorting a list
fruits.sort()

# Printing the final list
print("Updated list of fruits:", fruits)
