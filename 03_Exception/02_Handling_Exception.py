# age = int(input("Age : "))
# IF WE ENTER ANY VALUE OTHER THAN INTEGER WE WILLGET ERROR
# AS A PROGRAMMER ITS OUR RESPONSIBILITY TO THROW A VALID ERROR

try:
    age = int(input("Age : "))

except ValueError:
    print("Not a valid value ")

try:
    age = int(input("Age : "))

except ValueError as error:
    print("Not a valid value ")
    print(error)  # THE ERROR VARIABLE WILL STORE THE REASON OF ERROR
