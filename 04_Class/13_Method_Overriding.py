# class SetAge:
#     def __init__(self):
#         self.age = 20
#         print(self.age)


# class student1(SetAge):
#     def __init__(self):
#         self.weight = 50
#         print(self.weight)


# stud = student1()  # OTUPUT ---->>>> 50 ONLY THE RECENT CONSTRUCTOR WILL BR EXECUTED


class Gain:
    def __init__(self):
        print("Gain")


class lose(Gain):
    def __init__(self):
        super().__init__()
        print("Lose")


stud1 = lose()
