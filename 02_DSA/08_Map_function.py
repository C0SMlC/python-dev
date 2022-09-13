# num = [1, 2, 3, 4, 5]
# for numbers in num:
#     print(numbers)

items = [
    ("Product1", 10),
    ("Product2", 100),
    ("Product3", 1),
]
# print(items)
# print("\n")
# empty_List = []
# for item in items:
#     empty_List.append(item[1])

# print(empty_List)
x = list(map(lambda item: item[1], items))
print(x)
for xen in x:
    print(xen)
