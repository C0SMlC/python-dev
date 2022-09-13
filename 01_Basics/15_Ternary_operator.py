age = int(input("Enter your age : "))
if age >= 18:
    message = "Eligible"
else:
    message = "Not Eligible"

print(message)

print("You're eligible") if age >= 18 else print("Not eligible")
print("Up 18") if age >= 18 else print("Not Worthy")
