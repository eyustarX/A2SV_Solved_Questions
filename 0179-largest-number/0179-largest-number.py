class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if nums.count(0) == len(nums):
            return "0"
            
        nums = [str(i) for i in nums]
        num = sorted(nums, key=lambda x: x * (10 * 9), reverse= True)
        
        return "".join(num)