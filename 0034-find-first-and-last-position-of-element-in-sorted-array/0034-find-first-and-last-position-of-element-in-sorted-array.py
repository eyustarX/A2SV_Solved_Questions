class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        low = high = 0

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid - 1
            
            else:
                left = mid + 1
        low = left if left < len(nums) and nums[left] == target else -1
        
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid - 1
            
            else:
                left = mid + 1
        high = left - 1 if left - 1 >= 0 and nums[left - 1] == target else -1

        return [low, high]