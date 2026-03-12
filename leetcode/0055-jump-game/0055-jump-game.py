class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump = 0

        for num in nums:
            if jump < 0:
                return False
            
            elif num > jump:
                jump = num
            
            jump -= 1
        
        return True