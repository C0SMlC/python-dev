
class InvalidOperationError(Exception):
    pass


num = [1, 2, 3, 4, 5]
try:
    search = int(input("Num : "))

except ValueError:
    print("Not A Valid Value")
