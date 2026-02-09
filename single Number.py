class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        my_dict=Counter(nums)
        for key in my_dict:
            if my_dict[key]==1:
                return key
