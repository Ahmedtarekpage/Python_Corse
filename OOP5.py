class TagCloud:
    def __init__(self):
        self.dic = {}
        #dic = {"python" : 1 }

    def add(self, tag):
        self.dic[tag.lower()] = self.dic.get(tag.lower(), 0) + 1
        #self.dic["python"] = 3
    def __getitem__(self,tag):
      self.add(tag)
    def __setitem__(self, tag, count):
        self.dic[tag.lower()] = count
    def __len__(self):
        return len(self.dic)



cloud = TagCloud()
cloud.add("Python")
cloud.add("Python")
cloud.add("python")
cloud.add("Ahmed")
cloud["python"]
cloud["Ahmed"]
cloud["Seif"] = 10

print(len(cloud))


# cloud["pyfthon"] = 50
print(cloud.dic)
# print(len(cloud))
# print(cloud["pyfthon"])
