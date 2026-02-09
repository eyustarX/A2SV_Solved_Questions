class RandomizedSet:

    def __init__(self):
        self.count=set()

    def insert(self, val: int) -> bool:
        if val in self.count:
            return False
        else:
            self.count.add(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.count:
            self.count.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        for i in self.count:
            return i
        return self.count


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
