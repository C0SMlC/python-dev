values = []
for x in range(5):
    values.append(x*2)

print(values)

# or

values1 = {x*2 for x in range(5)}  # DICTIONARIES
print(values1)
values2 = {x*2 for x in range(5)}  # SET
print(values2)
values3 = {x: x*2 for x in range(1, 5)}
print(values3)
for x, y in values3.items():
    print(x, y)
