class Solution:
    def binaryGap(self, n: int) -> int:
        k = bin(n)[2:]
        gap = 0
        left = 0
        
        for i in range(1, len(k)):
            if k[i] == "1":
                gap = max(gap, i - left)
                left = i
        
        return gap
