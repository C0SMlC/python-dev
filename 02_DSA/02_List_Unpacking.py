numbers = [1, 2, 3]
nums = [1, 2, 3, 4, 5, 6]
# first = numbers[0]
# second = numbers[1]
# third = numbers[2]

# Value unpacking

first, second, third = numbers
print(first, second, third)
fir, remains, *last = nums
print(len(last))
print(last[0::])
print(fir, last)
print(remains)
