# def add(*num):
#     total = 0
#     for var in num:
#         total = var+total
#     return total


# num = 10
# print(add(1, 2, 3))
# print(num)


def another(**num):
    print(num)
    print(num["id"])
    print(num["name"])


another(id=1, name="Pratik")
