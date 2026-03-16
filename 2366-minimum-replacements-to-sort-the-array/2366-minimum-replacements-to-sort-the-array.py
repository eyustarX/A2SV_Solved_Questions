class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        count = 0

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > nums[i + 1]:
                k = (nums[i] + nums[i + 1] - 1) // nums[i + 1]
                nums[i] = nums[i] // k
                count += k - 1
        
        return count

