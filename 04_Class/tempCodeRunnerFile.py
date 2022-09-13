class TagCloud:
    def __init__(self):
        self.tags = {}

    def add(self, tag):
        self.__tags[tag] = self.__tags.get(tag, 0)+1

    def __getitem__(self, tag):
        return self.__tags.get(tag, 0)

    def __setitem__(self, tag, count):
        self.__tags[tag] = count

    def __len__(self):