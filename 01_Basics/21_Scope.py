num = 12
print(num)


def sum():
    global num  # will access the original element
    # num = 14  # copy variable
    print(num)
    num = 16
    print(num)


sum()
print(num)
