values = [
    ("Product1", 1),
    ("Product2", 2),
    ("Product3", 3),
]

x = list(map(lambda value: value[1], values))
print(*x)
y = list(filter(lambda var: var[1] >= 2, values))
z = list(map(lambda valu: valu[1], y))
print(*z)
