import os
import re

# 1. Create a text file with your full name
with open('philip_daudu.txt', 'w') as file:
    file.write('Philip Daudu')

# 2. Read the text file and extract first name, surname, and middle name
current_directory = os.getcwd()
file_path = os.path.join(current_directory, 'philip_daudu.txt')

with open(file_path, 'r') as file:
    full_name = file.read()

first_name, last_name = full_name.split()
surname = full_name[len(first_name):-len(last_name)].strip()

print("1. First Name:", first_name)
print("   Surname:", surname)
print("   File Path:", file_path)

# 3. Extract baby names from HTML files using Regex
html_content = """
<html>
  <body>
    <p>Baby names: Emma, Liam, Olivia, Noah</p>
  </body>
</html>
"""

baby_names_match = re.search(r'Baby names: (.+)</p>', html_content)
if baby_names_match:
    baby_names = baby_names_match.group(1).split(', ')
    print("\n2. Baby Names:", baby_names)
else:
    print("\n2. No baby names found.")

# 4. Create a simple sorting algorithm (Bubble Sort)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Example usage
numbers = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(numbers)
print("\n3. Sorted Numbers:", numbers)

# 5. Implement binary search
def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]

        if mid_value == target:
            return mid  # Found the target
        elif mid_value < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Target not found

# Example usage
sorted_numbers = [11, 12, 22, 25, 34, 64, 90]
target_number = 25
result = binary_search(sorted_numbers, target_number)

if result != -1:
    print("\n4. Target", target_number, "found at index", result)
else:
    print("\n4. Target", target_number, "not found.")
