# Variables and Types
# Understanding how to create variables and the different data types in Python.
# integers, floats, strings, booleans, lists, tuples, sets, dictionaries 

# Examples:
age = 25
name = "Sandeep Singh"
weight = 75.5
is_student = True

# print(name)
# print(age)
# print(weight)
# print(is_student)

groceries = ["milk", "eggs", "atta", "rice", "tea", "milk"]

# set contains unique values
set_groceries = set(groceries)

person = {"name": "Gursharn", "age": 25, "is_student": True}
skills = {"Python", "JavaScript", "Django", "Python"}
coordinates = (31.620737, 74.876605)

# print(groceries)


# Basic Operators
# Introduction to arithmetic, comparison, assignment, logical, and other operators in Python.

# Examples:
l = 10
w = 20
area = l * w
perimeter = 2 * (l + w)
is_square = l == w
is_rectangle = l != w
is_length_greater = l > w
is_length_lesses = l < w
is_length_greater_or_equal = l >= w
is_length_less_or_equal = l <= w
is_not_square = not is_square



# String Formatting
# Learn how to format strings using f-strings.

# Examples:
name = "Gursharn"
age = 25

# print(f"My name is {name} and I am {age} years old.")


# Basic String Operations
# Learn basic operations that can be performed on strings like slicing, concatenation, and common string methods.

# Examples:
name = "Gursharn Singh"
# print("first letter", name[0])
# print("last letter", name[-1])

first_name = name[:8]
# print("first name",  first_name)

last_name = name[9:]
# print("last name", last_name)

full_name = first_name + " " + last_name
# print("full name", full_name)

# print("length of name", len(name))

# print("uppercase", name.upper())
# print("lowercase", name.lower())
# print("titlecase", name.title())
# print("find", name.find("Singh"))
# print("replace", name.replace("Singh", "Kaur"))
# print("split", name.split(" "))
# print("startswith", name.startswith("Gursharn"))
# print("endswith", name.endswith("Singh"))


