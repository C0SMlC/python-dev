names = ["Pratik", "Tanvi", "jija"]
inp = input("Enter starting character : ")
end = input("Enter ending character : ")
for var in names:
    if var.startswith(inp[0]) and var.endswith(end[0]):
        print("Found")
        print(var)
        break
else:
    print("Not found")
