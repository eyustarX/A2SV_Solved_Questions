class Solution:
    def minElement(self, nums: List[int]) -> int:
        min_num = float('inf')

        for num in nums:
            value = 0
            while num > 0:
                value += (num % 10)
                num //= 10
            
            if value  < min_num:
                min_num = value
        
        return min_num
                