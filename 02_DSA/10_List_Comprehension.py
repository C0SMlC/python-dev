items = [
    ("Product1", 10),
    ("Product2", 100),
    ("Product3", 1),
]

prices = list([item[0] for item in items])
print(prices)
prices = list([item[1] for item in items if item[1] >= 10])
print(*prices)
