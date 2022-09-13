class Swim:

    def __init__(self) -> None:
        pass

    def swim(self):
        print("Can Swim")


class Fly:
    def fly(self):
        print("Can Fly")


class FlyingFish(Swim, Fly):
    print(Swim())


Fish = [FlyingFish(swim, fly)]
print(Fish)
