point = {"x": 1, "y": 2}
point = dict(x=1, y=2)
print(point["x"])
print(point)
if "x" in point:
    print(point["x"])
else:
    print("Invalid")

print(point.get("x", "Item not found"))
del point["x"]
print(point)
point = {"x": 1, "y": 2}
for key in point:
    print(key, point[key])

for x, y in point.items():
    print(x, y)
