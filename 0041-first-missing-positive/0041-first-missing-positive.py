class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            if num < 1:
                nums[i] = len(nums) + 1
        
        for num in nums:
            val = abs(num)
            if 1 <= val <= len(nums):
                nums[val - 1] = - abs(nums[val - 1])
        
        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1
        
        return len(nums) + 1