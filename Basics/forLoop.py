for i in range(3):
    print('Krishna Kamal Baishnab')







# **Python:**
# - `for` loops in Python are primarily used to iterate over iterable objects.
# - The syntax of a `for` loop in Python is simple and clean: `for item in iterable`.
# - Python's `for` loop does not require an explicit index variable or control statement.
# - Python's `for` loop is designed to be more intuitive and convenient for iterating over collections.

# **JavaScript:**
# - JavaScript's `for` loop shares similarities with C-style loops.
# - The syntax includes an initialization expression, a condition expression, and an update expression.
# - JavaScript's `for` loop can also iterate over iterable objects using constructs like `for...of`.
# - `for` loops in JavaScript are commonly used for array iteration and general looping tasks.

# **Java:**
# - Java's `for` loop is similar to C's syntax but has more features and is more robust.
# - Java's `for` loop syntax also includes an initialization expression, a condition expression, and an update expression.
# - Java's `for` loop is widely used for iterating over arrays and collections.

# **C++:**
# - C++'s `for` loop syntax is similar to C's syntax.
# - It includes an initialization expression, a condition expression, and an update expression.
# - C++'s `for` loop is often used for array iteration and general looping tasks.
# - C++ offers more control over loop execution through features like range-based `for` loops and iterators.

# In summary, while the basic functionality of `for` loops remains consistent across languages, the syntax and additional features may vary. Python's `for` loop syntax is designed to prioritize simplicity and readability, which may differ from the more explicit syntax found in languages like C, JavaScript, and Java.
    



number = input("Enter a number: ")

for i in range(1, 11):
    print(f"{number} x {i} = {int(number) * i}")