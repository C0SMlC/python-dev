from sys import getsizeof

# FOR LARGE DATA

values = {x: x*2 for x in range(10000)}
values1 = [x*2 for x in range(10000)]
values2 = (x*2 for x in range(10000))
print(type(values))
print(getsizeof(values))
print(type(values1))
print(getsizeof(values1))
print(type(values2))
print(getsizeof(values2))
# x = list(values2)
# print(x)
# OUTPUT

# <class 'dict' >
# 5242968
# <class 'list' >
# 800984
# <class 'generator' >
# 104
