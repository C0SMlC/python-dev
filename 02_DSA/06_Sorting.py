num = [12, 15, 1, 45, 2, 78]
num.sort()
print(num)
num.sort(reverse=True)
print(num)

numbers = [12, 28, 4, 6, 14, 87]
print(sorted(numbers))
print(sorted(numbers, reverse=True))

item = [
    ("Product1", 10),
    ("Product3", 100),
    ("Product2", 1),
]
# For sorting tuples


def sort_item(item):
    return item[1]


items1 = sorted(item, key=lambda keyvar: keyvar[1])
print(items1)
