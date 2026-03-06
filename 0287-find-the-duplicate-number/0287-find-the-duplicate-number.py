class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        slow = nums[i]
        fast = nums[i + 1]

        while i + 1 < len(nums):
            slow = nums[i]
            fast = nums[i + 1]

            if slow == fast:
                return slow
            i += 1
        
