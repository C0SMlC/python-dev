# CHECK IF TWO ROOKS CAN TACKLE EACH OTHER OR NOT

test_case = input("Enter the number of testcases : ")
for _ in test_case:
    x1, y1, x2, y2 = map(int, input("Enter co-ordinates (x,y) : ").split())
    if (x1 == x2) or (y1 == y2):
        print("Can Tackle")
    elif (x1 == x2) or (y1 == y2):
        print("Cant be on same location")
    else:
        print("Cant tackle")
