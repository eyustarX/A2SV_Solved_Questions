class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num)) > 1:
            num_list = [int(i) for i in str(num)]
            num = sum(num_list)
        
        return num
