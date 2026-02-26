class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        count = 0
        z =0
        l = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                z += 1
            
            while z > 1:
                if nums[l] == 0:
                    z -= 1
                
                l += 1
            
            count = max(count, r - l)

        return count

