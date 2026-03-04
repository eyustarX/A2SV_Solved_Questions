class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atMost(goal):
            curr = left = ans = 0

            for i in range(len(nums)):
                curr += nums[i]
                while curr > goal and left < len(nums):
                    curr -= nums[left]
                    left += 1
                
                ans += i - left +1
            return ans
            
        if goal > 0:
            return atMost(goal) - atMost(goal - 1)
        else:
            return atMost(goal)