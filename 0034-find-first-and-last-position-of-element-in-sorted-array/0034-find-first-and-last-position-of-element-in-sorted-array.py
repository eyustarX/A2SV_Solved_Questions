class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(left, right):
            if left > right:
                return [-1, -1]
            
            index = (left + right) // 2

            if nums[index] == target:
                k = y = index
                while k + 1 < len(nums) and nums[k + 1] == target:
                    k += 1
                while y - 1 >= 0 and nums[y - 1] == target:
                    y -= 1
                return [y, k]
                
            if nums[index] > target:
                return search(left, index - 1)
            else:
                return search(index + 1, right)
        
        return search(0, len(nums) - 1)