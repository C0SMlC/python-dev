class Properties:
    def name(self, name1):
        self.name1 = name1


class Animal(Properties):  # INHERITANCE -->>> PARENT CLASS "PROPERTIES"
    pass


class Bird(Properties):
    pass


person1 = Properties()
person1.name("Pratik")
print(person1.name1)
animal1 = Animal()
animal1.name("cat")
print(animal1.name1)
