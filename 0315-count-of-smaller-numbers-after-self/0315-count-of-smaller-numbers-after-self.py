class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sorted_list = []
        result = []
        
        for num in reversed(nums):
            pos = bisect.bisect_left(sorted_list, num)
            result.append(pos)
            bisect.insort(sorted_list, num)
        
        return result[::-1]