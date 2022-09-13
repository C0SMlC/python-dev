from abc import ABC, abstractmethod


class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class Textbox(UIControl):
    def draw(self):
        print("text")


class DropDownList(UIControl):
    def draw(self):
        print("List")


def draw(controls):
    for control in controls:
        control.draw()


ddl = DropDownList()
Text = Textbox()
draw([ddl, Text])
