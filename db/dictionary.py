# Creating a dictionary
student = {
    "name": "Alice",
    "age": 20,
    "grades": [85, 90, 78],
    "is_passing": True
}

# Accessing values in a dictionary
student_name = student["name"]
print("Student name:", student_name)

# Modifying values in a dictionary
student["age"] = 21

# Adding a new key-value pair to a dictionary
student["gender"] = "female"

# Removing a key-value pair from a dictionary
removed_grades = student.pop("grades")

# Iterating through key-value pairs in a dictionary
for key, value in student.items():
    print(f"{key}: {value}")

# Dictionary comprehension
squared_numbers_dict = {x: x**2 for x in range(5)}

# Checking if a key is in the dictionary
is_age_key_present = "age" in student


# Length of a dictionary
num_keys = len(student)

# Printing the final dictionary
print("Updated student dictionary:", student)
