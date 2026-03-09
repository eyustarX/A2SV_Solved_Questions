class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = 0
        ans = 0

        for num in nums:
            if num == 0:
                count += 1
            
            else:
                count = 0
            
            if count:
                ans += count
        
        return ans