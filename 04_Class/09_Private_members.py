

class TagCloud:

    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag] = self.__tags.get(tag, 0)+1

    def __getitem__(self, tag):
        return self.__tags.get(tag, 0)

    def __setitem__(self, tag, count):
        self.__tags[tag] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


cloud = TagCloud()
cloud.add("Python")
cloud.add("Pyrhon")
cloud.add("PYThon")
cloud.add("pyrhon")
cloud["PYThon"] = 10
try:
    print(cloud.__tags["PYTHON"])
except AttributeError:
    print("Not Available")

    # PROBLEM -->>  IT GIVES ERROR BECAUSE EVERYTHING OIS STORED IN LOWER CASE

    # WE NEED TO HID THE ATTRIBUTE print(cloud.__tags["PYTHON"])
    #  WE USE __ OPERATOR TO MAKE ATTRIBUTES PRIVATE
print(cloud.__dict__)
print(cloud._TagCloud__tags["PYTHON"])
# A WAY TO STILL ACCESS THE ELEMENT
