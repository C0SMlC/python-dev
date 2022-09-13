letters = ["P", "R", "A", "T"]
# Add

letters.append("I")
letters.insert(5, "K")
print(letters)


# Remove

letters.pop(5)
print(letters)
letters.remove("I")
print(letters)
del letters[1:7]
print(letters)
