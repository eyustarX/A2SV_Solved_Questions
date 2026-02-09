class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        my_dict=Counter(nums)
        n=len(nums)
        ans=[]
        for key in my_dict:
            if my_dict[key] > floor(n/3):
                ans.append(key)

        return ans
