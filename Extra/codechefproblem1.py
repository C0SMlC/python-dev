#  x moves 1 step
# y moves 2 steps
def positoin(x: int, y: int):
    while (x != y):
        x = x + 1
        y = y + 1
    else:
        print("YES")


chef = int(input("Chefs current position : "))
chef_frnd = int(input("Friend current position : "))
positoin(chef, chef_frnd)
