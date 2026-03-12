class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        curr_min = float('-inf')

        for num in reversed(nums):
            if num < curr_min:
                return True
            while stack and stack[-1] < num:
                curr_min = stack.pop()

            stack.append(num)
        
        return False