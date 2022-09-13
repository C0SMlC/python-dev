class Text(str):  # STR IS INBUILT CLASS AND WITH IT WE CAN ACCESS ALL THE INBUILT ATTRIBUTES OF STR
    def duplicate(self):
        return self + self


Name = Text("Pratik")
print(Name.duplicate())
print(Name.capitalize())
print(Name.upper())
