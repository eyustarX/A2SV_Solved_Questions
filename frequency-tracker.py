class FrequencyTracker:

    def __init__(self):
        self.count={}
        self.freq={}

    def add(self, number: int) -> None:
        old=self.count.get(number,0)
        new=old+1
        self.count[number]=new
        if old>0:
            self.freq[old]-=1
            if self.freq[old]==0:
                del self.freq[old]
        self.freq[new]=self.freq.get(new,0)+1

    def deleteOne(self, number: int) -> None:
        if number not in self.count:
            return
        
        value=self.count[number]
        self.count[number]-=1
        self.freq[self.count[number]]=self.freq.get(self.count[number],0)+1
        
        if self.count[number]==0:
            del self.count[number]
        self.freq[value]-=1
        
        if self.freq[value]==0:
            del self.freq[value]

    def hasFrequency(self, frequency: int) -> bool:
        if frequency in self.freq:
            return True
        return False

# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
