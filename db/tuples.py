# Creating a tuple
colors = ("red", "green", "blue")

# Accessing elements in a tuple
first_color = colors[0]
print("First color:", first_color)

# Iterating through a tuple
for color in colors:
    print(color)

# Tuple unpacking
x, y, z = colors

# Concatenating tuples
combined_colors = colors + ("yellow", "purple")

# Checking if an element is in the tuple
is_yellow_in_colors = "yellow" in combined_colors

# Length of a tuple
num_colors = len(colors)

# Printing the final tuple
print("Updated colors tuple:", combined_colors)
