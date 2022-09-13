items = [
    ("Product2", 10),
    ("Product1", 100),
    ("Product3", 1),
]

# lambda function
items.sort(key=lambda argment: argment[1])
print(items)
