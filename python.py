import random;
import psycopg2;
import numpy as np;


# Task 1: Which color of shirt is the mean color?
colors = {
    'green': [3, 1, 2, 2, 2],
    'yellow': [2, 0, 1, 1, 0],
    'brown': [1, 2, 1, 1, 1],
    'blue': [7, 7, 8, 8, 5],
    'pink': [1, 2, 1, 1, 0],
    'orange': [2, 2, 2, 1, 1],
    'cream': [1, 0, 0, 1, 0],
    'red': [1, 1, 3, 1, 3],
    'white': [3, 5, 2, 4, 5],
    'blew': [0, 1, 0, 0, 0],  
    'black': [0, 0, 0, 0, 1]
}

total_days = len(colors['green'])

# Calculate the mean frequency for each color
mean_frequencies = {color: sum(colors[color]) / float(total_days) for color in colors}

# Find the color with the frequency closest to the mean
mean_color = min(mean_frequencies, key=lambda x: abs(mean_frequencies[x] - total_days / 2))

print("Mean Color:", mean_color)

# Task 2: Which color is mostly worn throughout the week?
# Sum the frequencies for each color
total_frequencies = {color: sum(colors[color]) for color in colors}

# Find the color with the highest total frequency
most_worn_color = max(total_frequencies, key=total_frequencies.get)

print("Most Worn Color:", most_worn_color)

# Task 3: Which color is the median?
# Sort the frequencies for each color
sorted_frequencies = {color: sorted(colors[color]) for color in colors}

# Find the color with the median frequency
median_color = {color: sorted_frequencies[color][total_days // 2] for color in colors}

print("Median Color:", median_color)

# Task 4: BONUS Get the variance of the colors
# Get the variance of the frequencies for each color
variance_colors = {color: np.var(colors[color]) for color in colors}

print("Variance of Colors:", variance_colors)

# Task 5: BONUS If a color is chosen at random, what is the probability that the color is red?
# Calculate the probability of choosing the color red
probability_red = total_frequencies['red'] / float(total_days)

print("Probability of Choosing Red:", probability_red)

# Task 6: Save the colors and their frequencies in PostgreSQL database
# Connect to PostgreSQL
conn = psycopg2.connect(database="bbiyvdgncczyaqevmw9b", user="ucrd39hqgctchmx3deru", password="xLSy34EsOtHTre20VdGRw2EaAFeR0A", host="bbiyvdgncczyaqevmw9b-postgresql.services.clever-cloud.com", port="50013")
cursor = conn.cursor()

# Create a table to store colors and frequencies
cursor.execute("CREATE TABLE IF NOT EXISTS colors (color TEXT, frequency INTEGER)")

# Insert data into the table
for color, frequency in total_frequencies.items():
    cursor.execute("INSERT INTO colors (color, frequency) VALUES (%s, %s)", (color, frequency))

# Commit the changes and close the connection
conn.commit()
conn.close()

# Task 7: BONUS Write a recursive searching algorithm to search for a number entered by the user in a list of numbers
def recursive_search(target, numbers, index=0):
    if index == len(numbers):
        return -1  # Not found
    elif numbers[index] == target:
        return index  # Found
    else:
        return recursive_search(target, numbers, index + 1)

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
user_input = int(input("Enter a number to search: "))  # For Python 2.7

result = recursive_search(user_input, numbers_list)

if result != -1:
    print("Number found at index:", result)
else:
    print("Number not found in the list.")

# Task 8: Write a program that generates a random 4-digit number of 0s and 1s and converts the generated number to base 10
# Generate a random 4-digit binary number
binary_number = ''.join(random.choice('01') for _ in range(4))

# Convert binary to decimal
decimal_number = int(binary_number, 2)

print("Generated Binary Number:", binary_number)
print("Converted to Decimal:", decimal_number)

# Task 9: Write a program to sum the first 50 Fibonacci sequence
def fibonacci(n):
    fib_sequence = [0, 1]
    for _ in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

first_50_fibonacci = fibonacci(50)
sum_first_50_fibonacci = sum(first_50_fibonacci)

print("First 50 Fibonacci Sequence:", first_50_fibonacci)
print("Sum of the First 50 Fibonacci Sequence:", sum_first_50_fibonacci)
