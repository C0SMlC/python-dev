class Color:
    default_Color = "Red"

    def setColor(self, name: str):
        print(name)


print(Color.default_Color)
Color.default_Color = "Blue"
first = Color()
first.setColor("Cyan")
print(first.default_Color)
second = Color()
second.setColor("Yellow")
