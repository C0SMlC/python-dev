#  IN PYTHON EACH CLASS IS SUBCLASS OF BASE CLASS OBJECT

class animal:
    pass


A = animal()

print(issubclass(animal, object))  # TRUE
print(isinstance(A, animal))       # TRUE
