def caclculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cant be zero or less")
    return 10/age


try:
    caclculate_xfactor(int(input("age:")))
except ValueError as error:
    print("Age cant be zero or less")

# NOT RECCOMMENDED WAY OF THROW EXCEPTION
