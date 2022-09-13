from abc import ABC, abstractmethod

# class UIControl(ABC):  We dont need this class
#     @abstractmethod
#     def draw(self):
#         pass


class Textbox():
    def draw(self):
        print("text")


class DropDownList():
    def draw(self):
        print("List")


def draw(controls):
    for control in controls:
        control.draw()


ddl = DropDownList()
Text = Textbox()
draw([ddl, Text])  # as long as draw is iterable polymophism will be done
