# 1. Create a list of numbers from 1 to 10
# We can use the list() function with range to do this quickly
numbers = list(range(1, 11))

# 2. Extract the first five elements (indices 0 to 4)
# Slicing [0:5] takes elements from start up to (but not including) index 5
first_five = numbers[:5]

# 3. Reverse these extracted elements
# Using the [::-1] slicing trick is a very Pythonic way to reverse a list
reversed_five = first_five[::-1]

# 4. Print both the extracted list and the reversed list
print("Original List:", numbers)
print("Extracted (First Five):", first_five)
print("Reversed Extracted List:", reversed_five)