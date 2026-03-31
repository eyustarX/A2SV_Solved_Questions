class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(left, right):
            if left > right:
                return [-1, -1]
            
            index = (left + right) // 2

            if nums[index] == target:
                upper = lower = index
                while upper + 1 < len(nums) and nums[upper + 1] == target:
                    upper += 1
                while lower - 1 >= 0 and nums[lower - 1] == target:
                    lower -= 1
                return [lower, upper]
                
            if nums[index] > target:
                return search(left, index - 1)
            else:
                return search(index + 1, right)
        
        return search(0, len(nums) - 1)