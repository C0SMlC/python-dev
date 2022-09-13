try:
    with open("04_Cleaning_up.py") as file:
        print("OPENED")
    age = int(input("Age : "))
    div = 100/age
except (ValueError, NameError):
    print("Not a valid value ")
else:
    print("NO exception were thrown")
# WITH STATEMENT WILL AUTOMATICALLY CLOSE THE OPENED FILE
