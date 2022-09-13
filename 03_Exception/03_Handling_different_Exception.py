try:
    age = int(input("Age : "))
    div = 100/age
except ValueError:
    print("Not a valid value ")
else:
    print("NO exception were thrown")

# OUTPUT

# Age: 0
# Traceback(most recent call last):
#   File "f:\Python Development\03_Exception\03_Handling_different_Exception.py", line 3, in <module >
#   div = 100/age
# ZeroDivisionError: division by zero

# REVISED CODE

try:
    age = int(input("Age : "))
    div = 100/age
except (ValueError, ZeroDivisionError):
    print("Not a valid value ")
else:
    print("NO exception were thrown")
