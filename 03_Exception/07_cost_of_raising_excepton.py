from timeit import timeit
code = """ 
def caclculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cant be zero or less")
    return 10/age


try:
    caclculate_xfactor(0)
except ValueError as error:
    print("Age cant be zero or less")
    """
code1 = """ 
def caclculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cant be zero or less")
    return 10/age


try:
    caclculate_xfactor(0)
except ValueError as error:
    pass
    """
code2 = """ 
def caclculate_xfactor(age):
    if age <= 0:
        return none
    return 10/age

 xfact= caclculate_xfactor(0)
 if xfact == none:
     pass
    """
print("First code = ", timeit(code, number=1000))
print("First code = ", timeit(code1, number=1000))
print("First code = ", timeit(code2, number=1000))
