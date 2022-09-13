numbers = [1, 2, 3]
print(numbers)
print(*numbers)
values = list(range(5))
print(values)
values = [*range(5)]
print(*values)

#  UNPACKING DICTIONARIES

NUM = {"x": 1, "y": 2}
num2 = {"z": 4}
combined = {**NUM, **num2}
print(combined)
