# 1. Create a dictionary with student names and their marks
# Names are keys, and marks are values
gradebook = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 95,
    "Ethan": 88
}

# 2. Ask the user to input a student's name
search_name = input("Enter the student's name to look up their grade: ")

# 3. & 4. Retrieve marks or display an error message
# We use .get() because it prevents the program from crashing if the name isn't there
marks = gradebook.get(search_name)

if marks is not None:
    print(f"{search_name} scored: {marks}")
else:
    print(f"Sorry, '{search_name}' is not in the system.")