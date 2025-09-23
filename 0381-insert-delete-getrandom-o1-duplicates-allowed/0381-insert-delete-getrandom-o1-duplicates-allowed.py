class RandomizedCollection:

    def __init__(self):
        self.lst = []
        self.dict = defaultdict(list)

    def insert(self, val: int) -> bool:
        flag = True if val not in self.dict else False
        self.lst.append(val)
        self.dict[val].append(len(self.lst) - 1)
        return flag
    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False
        last_val = self.lst[len(self.lst)-1]
        location = self.dict[val].pop()
        if not self.dict[val]:
            del self.dict[val]
        self.dict[last_val].append(location)
        self.dict[last_val].remove(len(self.lst)-1)
        if not self.dict[last_val]:
            del self.dict[last_val]
        self.lst[location] = last_val
        self.lst.pop()
        return True

    def getRandom(self) -> int:
        if not self.lst:
            return 1
        return random.choice(self.lst)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()