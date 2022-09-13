x = 1
print(id(x))
x = x+1
print(id(x))
print("\n")
"""2278987727088
   2278987727120
   Two differnt outputs ie two different location"""
# Mutable tyepes
y = [1, 2, 3]
print(id(y))
y.append(4)
print(id(y))
print(y)
print(y[0])
