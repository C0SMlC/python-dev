num = int(input("Enter size of array : "))
array = []
i: int
for i in range(0, num):
    element = int(input("Enter number : "))
    array.append(element)

# print(array)

sort = sorted(array, reverse=True)
# print(sort)
highest_num = int(input("numbers to be searched : "))
for t in range(0, highest_num):
    print(sort[t])
