class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def search(left, right):
            if left > right:
                return -1

            index = (left + right) // 2
           
            if nums[index] == target:
                return index
            
            if nums[index] > target:
                return search(left, index - 1)
            else:
                return search(index + 1, right)
        
        return search(0, len(nums) - 1)