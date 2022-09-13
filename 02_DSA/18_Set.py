# used to get unique items from list

# numbers = 1, 2, 3, 4, 1, 2
# uniques = set(numbers)
# print(uniques)
# second = {1, 2, 3}
# second.add(5)
# second.remove(1)
# print(len(second))
# print(second)
first = {1, 2, 3, 4}
second = {1, 2, 5}
lol = [1, 2, 3, 4, 5]
Set = set(lol)
print(first | Set)
print(first | second)  # finds union of two sets
print(first & second)  # finds commmon of two sets
print(first - second)  # finds difference of two sets
print(second - first)
print(first)
