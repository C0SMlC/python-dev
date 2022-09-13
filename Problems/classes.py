class setter():
    def __eq__(m, n):
        return m == n

    def set(self, x, y):
        z = input("Enter username : ")
        if(z == "Pratik"):
            self.x = x
            self.y = y
        else:
            print("Wrong")

    def printer(self):
        print("Done")


set1 = setter()
set2 = setter()
set2.__eq__(10, 20)
a, b = map(int, input().split())
set1.set(a, b)
try:
    set1.printer()
except AttributeError:
    pass
