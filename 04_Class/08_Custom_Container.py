class TagCloud:
    def __init__(self):
        self.tags = {}

    def add(self, tag):
        self.tags[tag] = self.tags.get(tag, 0)+1

    def __getitem__(self, tag):
        return self.tags.get(tag, 0)

    def __setitem__(self, tag, count):
        self.tags[tag] = count

    def __len__(self):
        return len(self.tags)

    def __iter__(self):
        return iter(self.tags)  # TO MAKE DICTIONARY ITERABLE


cloud = TagCloud()
cloud.add("Python")
cloud.add("Pyrhon")
cloud.add("PYThon")
cloud.add("pyrhon")
cloud["PYThon"] = 10  # uses setitem magic method
var = cloud["Python"]  # uses getitem magic method
print(var)
print(cloud.tags)
